#----------------------------------------------------------------------------------------------------#
#  Title: Assignment 07
#  Description: Pickling and Structured Error Handling
#  ChangeLog: (Who, When, What)
#  JWinslow, 11-28-2022, Created Script
#  JWinslow, 12-01-2022, attempted formatting
#  JWinslow, 12-03-2022, added error handling
#----------------------------------------------------------------------------------------------------#

# -- Data -- #
import pickle # This imports code from another code file.

# -- Processing -- #

# *** Demonstrate Pickling ***

customer_id = int(input("\nEnter an Id Number: "))
customer_name = str(input("Enter a Name: "))
customer_list = [customer_id, customer_name]
print(customer_list)

# Store the data with the pickle.dump method

objFile = open("AppData.dat", "ab")
pickle.dump(customer_list, objFile)
objFile.close()

# Read the data back with the pickle.load method

objFile = open("AppData.dat", "rb")
objFileData = pickle.load(objFile)  # Loads one row of data.
objFile.close()
print(objFileData)

# *** Demonstrate Structured Error Handling ***
# try/except
try:
    num = float(input("\nEnter a number: "))
except:
    print("\nOops, something went wrong!")

