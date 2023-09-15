# Copyright (c) 2023, Taweechai Yuenyang and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document, DocStatus

class LibraryMembership(Document):
	 # check before submitting this document
    def before_submit(self):
        print(f"From Date: {self.from_date} To Date: {self.to_date}") 
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                # check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        
        if exists:
            frappe.throw("There is an active membership for this member")
