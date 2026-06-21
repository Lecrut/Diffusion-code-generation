import re
NAME_PATTERN = '\\b'

def search_contacts(contacts, query):
    matches = []
    regex = re.compile(NAME_PATTERN + re.escape(query) + NAME_PATTERN, re.IGNORECASE)
    for name, details in contacts.items():
        if regex.search(name):
            matches.append((name, details['phone'], details['email']))
    return matches
if __name__ == '__main__':
    contacts = {'Alice Johnson': {'phone': '123-456-7890', 'email': 'alice@example.com'}, 'Bob Smith': {'phone': '098-765-4321', 'email': 'bob@example.com'}}
    query = 'li'
    results = search_contacts(contacts, query)
    for name, phone, email in results:
        print(f'Name: {name}, Phone: {phone}, Email: {email}')