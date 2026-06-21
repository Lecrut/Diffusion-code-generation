import re

def search_contacts(contacts, pattern):
    results = []
    regex = re.compile(pattern, re.IGNORECASE)
    for name, details in contacts.items():
        if regex.search(name):
            results.append((name, details))
    return results

if __name__ == '__main__':
    contacts = {
        "Alice Johnson": {"phone": "123-456-7890", "email": "alice.johnson@example.com"},
        "Bob Smith": {"phone": "987-654-3210", "email": "bob.smith@sample.org"}
    }
    search_pattern = "li"
    search_results = search_contacts(contacts, search_pattern)
    for name, details in search_results:
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")