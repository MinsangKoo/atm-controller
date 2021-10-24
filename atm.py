#import APIs

class ATM:
	def __init__(self):
		self.card_number = None
		self.bank_card = None
		self.account_type = None #1 for savings, 2 for checking
		self.transaction_type = None
		self.balance = 7000

	def readCard(self):
		#Case where card is incompatible with ATM. Let us assume any card number starting with 0 is not compatible.
		#For testing purposes, takes console input as card number.
		self.card_number = input("Insert Card: \n")

		if self.card_number[0] == "0":
			print("Your card cannot be used at this ATM.")
			self.ejectCard()

		#Case where card issuer is from a different bank. Let us assume our bank's cards always start with 5
		elif self.card_number[0] != "5":
			print("Card Accepted.")
			self.bank_card = False

		#Case where card is from this bank
		else:
			print("Card Accepted.")
			self.bank_card = True

	def checkPin(self):
		#apiCheckPin() is a function that would tell us whether the entered PIN was correct for the card. This function would be defined elsewhere.
		#User has 3 tries to enter the correct PIN. 
		remaining_tries = 3

		#getPin() reads PIN from ATM. This function would be defined elsewhere.
		while True:
			print("Enter PIN: ")
			pin_number = self.getKeypad()

			#If PIN is correct
			if self.apiCheckPin(self.card_number, pin_number):
				print("PIN Accepted")
				break

			#If user gets PIN wrong
			elif remaining_tries > 1:
				remaining_tries -= 1
				print("Incorrect PIN, you have " + str(remaining_tries) + " tries remaining")

			#If user exceeds 3 tries.
			else:
				print("Too many incorrect attempts.")
				self.ejectCard()

	def selectAccount(self):
		#User chooses between savings account and checking account.
		while True:
			self.account_type = input("For savings account, press 1. For checking account, press 2: ")
			if self.account_type == "1":
				print("You have selected savings account.")
				return
			elif self.account_type == "2":
				print("You have selected checking account.")
				return
			else:
				print("Invalid selection, please try again.")

	def apiCheckPin(self, card_number, pin_number):
		#Real world function would query a database for the card's pin number and compare it to the given pin_number.
		#For testing purposes, function returns True or False.
		return True
		#return False

	def ejectCard(self):
		#Function to close program.
		print("Ejecting card.")
		exit()

	def getKeypad(self):
		#Function would get number combination from the ATM's physical keypad.
		#For testing purposes, returns whatever user inputs in console.
		entered_pin = input()
		return entered_pin

	def selectTransaction(self):
		type_dict = {"1": "balance check.", "2": "deposit.", "3": "withdrawal."}
		while True:
			print("To check your balance, press 1.")
			print("To make a deposit, press 2")
			print("To make a withdrawal, press 3")
			self.transaction_type = self.getKeypad()
			if self.transaction_type not in type_dict:
				print("Invalid selection, please try again.")
			else:
				print("You have selected " + type_dict[self.transaction_type])
				return

	def performTransaction(self):
		if self.transaction_type == "1":
			self.checkBalance()
		elif self.transaction_type == "2":
			self.makeDeposit()
		elif self.transaction_type == "3":
			self.makeWithdrawal()
		print("Thank you for using this ATM")
		self.ejectCard()

	def apiCheckBalance(self):
		#Real world function would pull balance from account database.
		#For testing purposes, it will return a pre-defined number.
		return self.balance

	def checkBalance(self):
		acc_balance = self.apiCheckBalance()
		print("Your balance is: " + str(acc_balance))
		return acc_balance

	def openTray(self):
		#Function controls physical money tray.
		#For testing purposes, assume console input for money count.
		#Open
		#Close when user presses button.
		#Count money
		accepted_money = input()
		return int(accepted_money)

	def adjustBalance(self, adjustment_val):
		#Real world function would change database values.
		#For testing purposes, assume balance is 7000. Takes an integer
		self.balance = self.balance + adjustment_val

	def makeDeposit(self):
		print("Please insert your cash now.")
		deposit_amount = self.openTray()
		self.adjustBalance(deposit_amount)
		print("Your balance is now " + str(self.balance))

	def makeWithdrawal(self):
		print("How much would you like to withdraw?")
		withdrawal_amount = self.getKeypad()
		self.adjustBalance(int(withdrawal_amount) * -1)
		print("Your balance is now " + str(self.balance))


if __name__ == "__main__":
	Controller = ATM()
	Controller.readCard()
	Controller.checkPin()
	Controller.selectAccount()
	Controller.selectTransaction()
	Controller.performTransaction()
