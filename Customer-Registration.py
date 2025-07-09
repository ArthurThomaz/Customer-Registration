class Customer: # Stores all customer data.
    def __init__(self, cpf, name, surname, birthdate, gender, family_income):
        self.cpf = cpf
        self.name = name
        self.surname = surname
        self.birth_date = birthdate
        self.gender = gender.upper()  # gender.upper() = Converts input to uppercase
        self.family_income = float(family_income)  # (float) = Converts to numerical value

    def __str__(self): # Defines how customer data is displayed when printed
        return (
            f"\nCPF: {self.cpf}\nName: {self.name} {self.surname}\n"
            f"Birth Date: {self.birth_date}\nGender: {self.gender}\n"
            f"Income: R${self.family_income:.2f}\n"  # (.2f) formats as currency
        )

class CustomerRegistrationSystem: # Manages customer records.
    def __init__(self):
        self.customers = []  # Empty list to store customer objects

    def add_customer(self, customer): # Add customer
        if self.search_by_cpf(customer.cpf):  # Checks if the CPF is in the list
            print(f"Error: CPF {customer.cpf} already exists.")
            return False
        self.customers.append(customer)  # Adds new customer to list
        print(f"Customer {customer.cpf} added.")
        return True

    def list_customers(self): # Displays all registered customers
        if not self.customers:  # Checks if list is empty
            print("No customers registered.")
            return
        print("\nCUSTOMERS")
        for idx, customer in enumerate(self.customers, 1): # List the registered customers
            print(f"{idx}: {customer.name} {customer.surname}")

    def search_by_cpf(self, cpf): # Search customer by CPF
        for customer in self.customers:  # Checks each customer registered
            if customer.cpf == cpf:  # Compares CPF values
                return customer  # Returns match
        return None  # No match found

    def remove_customer(self, cpf): # Deletes customer by CPF
        customer = self.search_by_cpf(cpf)  # Finds customer first
        if customer:
            self.customers.remove(customer)  # Deletes from list
            print(f"Customer {cpf} deleted.")
            return True
        print(f"CPF {cpf} not found.")  # Error if not found
        return False

def main():
    system = CustomerRegistrationSystem()  # Creates our system

    # Continuous menu loop
    while True:
        # Display menu options
        print("\nCUSTOMER REGISTRATION")
        print("(1) - Add Customer")
        print("(2) - List All Customers")
        print("(3) - Search by CPF")
        print("(4) - Remove Customer")
        print("(5) - Exit")

        choice = input("Choose an option: ")

        # Option 1: Add new customer
        if choice == "1":
            print("\n[ NEW CUSTOMER ]")  # Collect customer details
            cpf = input("CPF: ").strip()  # Remove extra spaces
            name = input("First Name: ").strip()
            surname = input("Surname: ").strip()
            birth_date = input("Birth Date (DD/MM/YYYY): ").strip()
            gender = input("Gender (M/F/O): ").strip().upper()  # Standardize for uppercase
            income = input("Monthly Income (R$): ").strip()
            # Create and add customer
            new_customer = Customer(cpf, name, surname, birth_date, gender, income)
            system.add_customer(new_customer)

        elif choice == "2":  # List customers
            system.list_customers()

        elif choice == "3":  # Search by CPF
            cpf = input("Enter CPF to search: ").strip()
            customer = system.search_by_cpf(cpf)
            if customer:
                print("\n[ CUSTOMER FOUND ]")
                print(customer)  # Uses Customer format
            else:
                print("Customer not found.")

        elif choice == "4":  # Remove customer
            cpf = input("Enter CPF to remove: ").strip()
            system.remove_customer(cpf)

        elif choice == "5":  # Exit program
            print("Exiting system...")
            break
        else:  # Handle invalid choices
            print("Invalid choice. Choose between '1 - 5'.")

# Program
if __name__ == "__main__":
    main()  # Start the application