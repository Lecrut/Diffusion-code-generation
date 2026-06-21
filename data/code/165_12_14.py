import re

def search_contacts(contacts, query):
    pattern = re.compile(query, re.IGNORECASE)
    matching_contacts = {name: details for name, details in contacts.items() if pattern.search(name)}
    return matching_contacts

if __name__ == '__main__':
    sample_contacts = {
        "John Doe": {"phone": "123-456-7890", "email": "john.doe@example.com"},
        "Jane Smith": {"phone": "987-654-3210", "email": "jane.smith@example.com"},
        "Alice Johnson": {"phone": "555-555-5555", "email": "alice.johnson@example.com"}
    }
    
    query = "Jo"
    results = search_contacts(sample_contacts, query)
    print("Matching Contacts:")
    for name, details in results.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")