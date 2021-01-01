@http.route(['/update_partner'], type='json', auth="public", methods=['POST'], website=True)
def _check_registration_form(self, **values):
	"""
	Thic function to check the registration form data from the web site
	"""
	data = values
	registrant = data['registrant']
	check_matched = 0

	for index in range(0,len(Contactslist)):
		if registrant['email'] == Contactslist[index]['email']:
			check_matched = 1
		if registrant['phone'] == Contactslist[index]['phone']:
			check_matched = 1
	for index in range(0,len(leadslist)):
		if registrant['email'] == leadslist[index]['email']:
			check_matched = 1
		if registrant['phone'] == leadslist[index]['phone']:
			check_matched = 1 
	if check_matched == 0:
		Contactslist.appends(registrant)
