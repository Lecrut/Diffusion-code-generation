import re

def search_contacts(contacts, query):
    results = []
    for name, details in contacts.items():
        if re.search(query, name, re.IGNORECASE):
            results.append((name, details))
    return results

if __name__ == '__main__':
    sample_contacts = {
        "Alice Johnson": {"phone": "123-456-7890", "email": "alice.j@example.com"},
        "Bob Smith": {"phone": "987-654-3210", "email": "bob.s@example.net"},
        "Charlie Brown": {"phone": "555-555-5555", "email": "charlie.b@sample.org"}
    }
    
    query = "li"
    matches = search_contacts(sample_contacts, query)
    for match in matches:
        print(f"Name: {match[0]}, Phone: {match[1]['phone']}, Email: {match[1]['email']}")