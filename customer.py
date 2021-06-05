# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 07:28:14 2020

@author: S.Narain Ramaswamy
"""

class Customers:
    def __init__(self,strcusname,strcusemail,strcustype,strcusadd):
        self.strcusname = strcusname
        self.strcusemail = strcusemail
        self.strcustype = strcustype
        self.strcusadd = strcusadd
    def displayDetails(self):
        print("Name: ",self.strcusname)
        print("Email: ",self.strcusemail)
        print("Type: ",self.strcustype)
        print("Address: ",self.strcusadd)
        
yes = 1
while(yes):
    
    print("Enter the customer details: ")
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    type1 = input("Enter the type: ")
    address = input("Enter the address: ")
    c = Customers(name,email,type1,address)
    c.displayDetails()
    yes = int(input("Do you want to continue(1.Yes/0.No)"))


        

        
        