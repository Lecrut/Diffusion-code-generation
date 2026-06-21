import re

def search_contacts(query):
    results = []
    for name in contact_book:
        if re.search(re.escape(query), name, re.IGNORECASE):
            results.append(contact_book[name])
    return results

if __name__ == '__main__':
    contact_book = {
        'Alice Johnson': {'phone': '123-456-7890', 'email': 'alice@example.com'},
        'Bob Smith': {'phone': '987-654-3210', 'email': 'bob@example.com'}
    }
    query = 'li'
    print(search_contacts(query))