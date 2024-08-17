import json

# File to store contact data
CONTACT_FILE = 'file.json'

def load_contacts():
    """Load contacts from a JSON file."""
    try:
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    email = input("Enter contact email: ").strip()
    address = input("Enter contact address: ").strip()
    
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print("Contact added successfully.")

def view_contacts(contacts):
    """View all contacts."""
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts found.")

def search_contact(contacts):
    """Search for a contact by name or phone number."""
    search_term = input("Enter name or phone number to search: ").strip()
    
    found = False
    for name, details in contacts.items():
        if search_term in name or search_term in details['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
    
    if not found:
        print("No contact found with the given search term.")

def update_contact(contacts):
    """Update an existing contact."""
    name = input("Enter the name of the contact to update: ").strip()
    
    if name in contacts:
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email: ").strip()
        address = input("Enter new address: ").strip()
        
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ").strip()
    
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
