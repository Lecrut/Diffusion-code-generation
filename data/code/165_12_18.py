import re

def search_contacts(contacts, query):
    query = query.lower()
    results = [contact for contact in contacts if re.search(query, contact['name'], re.IGNORECASE)]
    return results

def main():
    contacts = [
        {'name': 'Alice Johnson', 'phone': '123-456-7890', 'email': 'alice.johnson@example.com'},
        {'name': 'Bob Smith', 'phone': '987-654-3210', 'email': 'bob.smith@example.com'},
        {'name': 'Charlie Davis', 'phone': '555-555-5555', 'email': 'charlie.davis@example.com'}
    ]
    
    query = "li"
    results = search_contacts(contacts, query)
    print("\n--- Search Results ---")
    for result in results:
        print(f"Name: {result['name']}, Phone: {result['phone']}, Email: {result['email']}")
    print("----------------------")

if __name__ == '__main__':
    main()