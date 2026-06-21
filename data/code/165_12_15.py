import re

def search_contacts(contacts, pattern):
    return [contact for contact in contacts if re.search(pattern, contact, re.IGNORECASE)]

if __name__ == '__main__':
    contacts = ["Alice Johnson", "Bob Smith", "Charlie Brown"]
    pattern = "li"
    results = search_contacts(contacts, pattern)
    print(results)