#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd



admin={"Pooja": "Pooja2210"}

inventory = {1: {'Name': 'Tandoori Chicken', 'FoodID': 1,'Quantity': '4 pieces', 'Price': 240,'Discount':10, 'Stock': 30},
             2: {'Name': 'Vegan burger', 'FoodID': 2,'Quantity': '1 pieces', 'Price': 320,'Discount':10, 'Stock': 20},
             3: {'Name': 'Truffle Cake', 'FoodID': 3,'Quantity': '500 gm', 'Price': 900,'Discount':20, 'Stock': 15}}


def Add_new_food_item():
    Name = input("Enter the food name you want to add :: ")
    FoodID = max(inventory.keys())+1
    Quantity = input("Enter the quantity per portion :: ")
    price = int(input("Enter the price per portion:: "))
    Discount = int(input("Enter the percentage of discount on this particular item :: "))
    stock = int(input("Enter amount left in stock in the restaurant :: "))
    
    inventory[FoodID]={
        'Name':Name,
        'FoodID':FoodID,
        'Quantity':Quantity,
        'Price':price,
        'Discont':Discount,
        'Stock':stock
        }
    print('\n')
    print("The fooditem {} is added to the Inventory".format(Name))
    return inventory


def edit_food_item():
    for i in inventory:
        print(i,inventory[i])
    i=int(input("Enter which Food item id you want to edit :: "))
    if i  not in inventory.keys():
        i=int(input("The item id does not exist ,Renter which Food item id you want to edit :: "))
    Name = input("Enter the food name you want to add :: ")
    Quantity = input("Enter the quantity per portion :: ")
    price = int(input("Enter the price per portion:: "))
    Discount = int(input("Enter the percentage of discount on this particular item :: "))
    stock = int(input(" Enter amount left in stock in the restaurant ::"))
    inventory[i]['Name'] = Name
    inventory[i]['Quantity']=Quantity
    inventory[i]['Price']=price
    inventory[i]['Discount']=Discount
    inventory[i]['Stock']=stock
    print("The food item {} is successfully edited".format(Name))
    return inventory


def view_inventory():
    print("*****The inventory includes*****")
    inv=pd.DataFrame(inventory)
    print(inv)
    
def remove_food_item():
    for i in inventory:
        print(i,inventory[i])
    foodid=int(input("Enter the food id which you want to remove from the above table"))
    if foodid  not in inventory.keys():
        foodid=int(input("The item id does not exist ,Renter which Food item id you want to edit :: "))
    inventory.pop(foodid)
    print("The food item is successfully removed") 
    
    
import admin as ad
class user: 
    
    login_info={"Pooja":"Pooja2210","Pooja1":"Pooja2211"}
    order_history={}
    profile = {}
    
    
    def __init__(self,fullname,phonenumber,email,address,password):
        self.fullname = fullname
        self.phonenumber=phonenumber
        self.email=email
        self.addresss=address
        self.password=password
    
        
        
        
    @classmethod    
    def signup(cls,fullname,phonenumber,email,address,username,password):
        user.profile[username]={
            "fullname":fullname,
            "phonenumber":phonenumber,
            "email":email,
            "address":address,
            "username":username,
            "password":password,
            }
        user.login_info[username]=password
        print('\n')
        print("  You have successfully registered . Now you can login  ")
        return user.profile
    
    @classmethod
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            print("   You're are successfully logged in   ")
            return True
        else:
            print("   SORRY! These are the Wrong Credentials   ")
            return False
        
    
    
    
    def place_new_order(self,username):
        Place_order_crawler = True
        while Place_order_crawler:
            l=[]
            print("Select items from below inventory ::")
            print("_______________________________")
            for i in ad.inventory:
                print("{}. {} ({}) [INR {} ]".format(ad.inventory[i]['FoodID'],ad.inventory[i]['Name'],ad.inventory[i]['Quantity'],ad.inventory[i]['Price']))
            a=list(map(int,input("Select the item id which you want to buy separated by comma :: ").split(',')))
            total=0
            for i in a:
                price=0
                b=int(input("Howmany {} you want to buy ".format(ad.inventory[i]['Name'])))
                price+=ad.inventory[i]['Price']*(1-(ad.inventory[i]['Discount']/100))*b
                total+=price
                l.append([ad.inventory[i]['Name'],b,ad.inventory[i]['Price'],ad.inventory[i]['Discount'],price])
            user.order_history[username]=l
            print('\n')
            print("The cart is as follows :: ")
            print("Username :: {}".format(username))
            print('____________________________________')
            for i in user.order_history[username]:
                print("{}--{}Nos--{}INR".format(i[0],i[1],i[4]))
            print('_____________________________________')
            print('Total amount you have to paid {}'.format(total))
            print("Do you want to update your order ?")
            m=int(input("1.Yes 2.No"))
            if m==2:
                Place_order_crawler=False
        k=int(input("Select Place your order option :: \n 1.Place your order"))
        if k==1:
            print('\n')
           
            print("********************* Your order is placed successfully . ********************* ")
        return True

        
    def order_history_(self,username):
        total=0
        for i in self.order_history[username]:
            total+=i[4]
            print("Name :: {}".format(i[0]))
            print("________________________________________________________")
            print("Quantity :: {}".format(i[1]))
            print("Price/Quantity:: {}".format(i[2]))
            print("Discount :: {}".format(i[3]))
            print("Toatal price after discount :: {}".format(i[4]))
            print('\n')
        print("Total amount {}".format(total))
        return user.order_history
            
            


    def update_profile(self,username):
        fullname=input("Enter your name :: ")
        phonenumber=int(input("Enter your phone number :: "))
        email = input("Enter your email id :: ")
        address=input("Enter your address :: ")
        password=input("Enter your password :: ")
        user.profile[username]={
            "fullname":fullname,
            "phonenumber":phonenumber,
            "email":email,
            "address":address,
            "password":password,
            }
        print('\n')
        print("You have successfully updated your profile ")
        return user.profile
    
import admin as ad
from user import user
import pandas as pd

uhh=user(str,int,str,str,str)



inputt= int(input("Enter a number 1:Admin 2:user 3:exit"))
if inputt==1:
    print("Welcome to the admin panel")
    username = input("Enter the username ::")
    password = input("enter the password ::")
    if ad.admin_user[username]==password:
        print("**********  You are successfully logged in as admin user  **********")
        admin_crawler = True
        while admin_crawler:
            s = int(input('Enter an option \n 1:Add new food item \n 2:edit food item \n 3:view inventory \n 4:remove food item  \n 5:exit \n'))
            if s==1:
                ad.Add_new_food_item()
            elif s==2:
                ad.edit_food_item()
            elif s==3:
                ad.view_inventory()
            elif s==4:
                ad.remove_food_item()
            elif s==5:
                print("{}, You are logged out ".format(username))
                admin_crawler=False
            else:
                print("Please select the wright option ")
    else:
        print("The username and passwords is incorrect")
            
elif inputt==2:
    
    print("********************  WELCOME TO THE USER PANEL  ********************")
    
    fullname=input("Enter your name :: ")
    phonenumber=int(input("Enter your phone number :: "))
    email = input("Enter your email id :: ")
    address=input("Enter your address :: ")
    username=input("Enter a user name :: ")
    while username in user.login_info.keys():
        print("Please try another username , this username is already existed")
        username=input("Enter a new user name :: ")
    password=input("Enter your password :: ")
    
    
    if user.signup(fullname,phonenumber,email,address,username,password):
        
        print("**********************  WELCOME TO THE LOGIN PANEL  *********************")
        
        username = input("Enter your username : ")
        password = input("Enter your password : ")
        if user.login(username, password):
            print(" Done :) ! ")
            user_crawler=True
            while user_crawler:
                user_choice = int(input("Please enter a choice \n 1:Place new order \n 2:order history \n 3:update profile \n 4:exit \n"))
                if user_choice==1:
                    uhh.place_new_order(username)
                if user_choice==2:
                    uhh.order_history_(username)
                if user_choice==3:
                    uhh.update_profile(username)
                if user_choice==4:
                    print("Thank you for shopping with us ")
                    user_crawler = False
else:
    print("Thank you ! Visit again : ) ")
    



# In[ ]:




