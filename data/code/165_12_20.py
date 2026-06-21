import re

class ContactSearch:
    CONTACTS = {
        "Alice Johnson": {"phone": "123-456-7890", "email": "alice@example.com"},
        "Bob Smith": {"phone": "987-654-3210", "email": "bob@example.com"}
    }

    @staticmethod
    def search_contacts(query):
        pattern = re.compile(re.escape(query), re.IGNORECASE)
        matches = [name for name in ContactSearch.CONTACTS if pattern.search(name)]
        return matches

if __name__ == '__main__':
    query = "alice"
    results = ContactSearch.search_contacts(query)
    print(results)