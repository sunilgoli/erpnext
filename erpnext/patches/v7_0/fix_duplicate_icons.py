import frappe

from frappe.desk.doctype.desktop_icon.desktop_icon import (sync_desktop_icons,
	get_desktop_icons, set_hidden)

def execute():
	'''hide new style icons if old ones are set'''
	sync_desktop_icons()

	for user in frappe.get_all('User', filters={'user_type': 'System User'}):
		desktop_icons = get_desktop_icons(user.name)
		icons_dict = {}
		for d in desktop_icons:
			if not d.hidden:
				icons_dict[d.module_name] = d

		for key in (('Selling', 'Customer'), ('Stock', 'Item'), ('Buying', 'Supplier'),
			('HR', 'Employee'), ('CRM', 'Lead'), ('Support', 'Issue'), ('Projects', 'Project')):
			if key[0] in icons_dict and key[1] in icons_dict:
				set_hidden(key[1], user.name, 1)
