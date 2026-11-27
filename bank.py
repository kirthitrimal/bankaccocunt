
# Bank Account Management

name = input("Enter customer name: ")
balance = float(input("Enter initial account balance: "))

print("\n----- BANK ACCOUNT DETAILS -----")
print("Customer Name:", name)
print("Initial Balance: Rs.", balance)

deposit = float(input("\nEnter deposit amount: "))
balance = balance + deposit

print("Balance after deposit: Rs.", balance)

withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal successful.")
else:
    print("Insufficient balance.")

print("Updated Account Balance: Rs.", balance)
