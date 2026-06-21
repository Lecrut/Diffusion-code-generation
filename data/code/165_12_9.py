import re

def search_contacts(contacts, query):
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    return [contact for contact in contacts if pattern.search(contact)]
if __name__ == '__main__':
    contacts = ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince']
    query = 'li'
    results = search_contacts(contacts, query)
    print(results)