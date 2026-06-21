import re

class ContactSearch:
    CONTACTS = [
        ("Alice Johnson", "123-456-7890", "alice.johnson@example.com"),
        ("Bob Smith", "987-654-3210", "bob.smith@example.com"),
        ("Charlie Brown", "555-555-5555", "charlie.brown@example.com")
    ]

    @staticmethod
    def search_contacts(query):
        pattern = re.compile(re.escape(query), re.IGNORECASE)
        results = [contact for contact in ContactSearch.CONTACTS if any(pattern.search(part) for part in contact)]
        return results

if __name__ == '__main__':
    query = "li"
    matching_contacts = ContactSearch.search_contacts(query)
    print(matching_contacts)