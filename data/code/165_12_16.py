import re

class ContactSearch:
    CASE_INSENSITIVE_FLAG = re.IGNORECASE
    
    @staticmethod
    def search_contacts(contacts, query):
        pattern = re.compile(query, flags=ContactSearch.CASE_INSENSITIVE_FLAG)
        return [contact for contact in contacts if pattern.search(contact['name'])]

if __name__ == '__main__':
    contacts = [
        {'name': 'Alice Johnson', 'phone': '123-456-7890', 'email': 'alice@example.com'},
        {'name': 'Bob Smith', 'phone': '987-654-3210', 'email': 'bob@example.com'},
        {'name': 'Charlie Brown', 'phone': '555-555-5555', 'email': 'charlie@example.com'}
    ]
    
    query = 'li'
    results = ContactSearch.search_contacts(contacts, query)
    print(results)