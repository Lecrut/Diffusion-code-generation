def contact_generator(city, page_size=10):
    contacts = [
        {"name": "Alice", "city": "New York"},
        {"name": "Bob", "city": "Los Angeles"},
        {"name": "Charlie", "city": "Chicago"},
        {"name": "David", "city": "New York"},
        {"name": "Eve", "city": "Los Angeles"}
    ]
    
    for i in range(0, len(contacts), page_size):
        yield [contact for contact in contacts[i:i+page_size] if contact["city"] == city]

if __name__ == '__main__':
    gen = contact_generator("New York")
    print(next(gen))
    print(next(gen))