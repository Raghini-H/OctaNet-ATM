class ATM:
    def __init__(self, pin, bal=0):
        self.pin = pin
        self.bal = bal
        self.history = []

    def authen(self):
        #Prompts the user to enter their PIN for authentication.
        enter = input("Enter your PIN: ")
        return enter == self.pin

    def check(self):
        #Displays the current account bal.
        print(f"Your current bal is: ${self.bal}")
        self.history.append("Checked account bal")

    def deposit(self):
        #Allows the user to deposit cash into their account.
        try:
            a = float(input("Enter the amount to deposit: "))
            if a > 0:
                self.bal += a
                print(f"${a} has been deposited into your account.")
                self.history.append(f"Deposited ${a}")
            else:
                print("Enter a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw(self):
        #Allows the user to withdraw cash from their account.
        try:
            a = float(input("Enter the amount to withdraw: "))
            if a > 0:
                if a <= self.bal:
                    self.bal -= a
                    print(f"You have withdrawn ${a}.")
                    self.history.append(f"Withdrew ${a}")
                else:
                    print("Insufficient funds.")
            else:
                print("Enter a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def change_pin(self):
        #Allows the user to change their PIN.
        new = input("Enter your new PIN: ")
        confirm = input("Re-enter your new PIN to confirm: ")
        if new == confirm:
            self.pin = new
            print("Your PIN has been successfully changed.")
            self.history.append("PIN changed")
        else:
            print("PINs do not match. Try again.")

    def view_transaction_history(self):
        #Displays the transaction history.
        if self.history:
            print("Transaction History:")
            for t in self.history:
                print(f"- {t}")
        else:
            print("No transactions available.")

    def run(self):
        #Runs the ATM simulation.
        if not self.authen():
            print("Authentication failed. Exiting...")
            return

        while True:
            print("\nATM Menu:")
            print("1. Check balance")
            print("2. Deposit Cash")
            print("3. Withdraw Cash")
            print("4. Change PIN")
            print("5. View Transaction History")
            print("6. Exit")

            try:
                choice = int(input("Select an option: "))
                if choice == 1:
                    self.check()
                elif choice == 2:
                    self.deposit()
                elif choice == 3:
                    self.withdraw()
                elif choice == 4:
                    self.change_pin()
                elif choice == 5:
                    self.view_transaction_history()
                elif choice == 6:
                    print("Thank you for using the ATM")
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# Main program
if __name__ == "__main__":
    # Create an instance of the ATM with an initial PIN and optional bal
    my_atm = ATM(pin="1234", bal=1000.0)
    my_atm.run()
