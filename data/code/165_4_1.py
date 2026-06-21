def contact_generator(city, page_size=10):
    contacts = [
        {"name": "Alice", "city": "New York"},
        {"name": "Bob", "city": "Los Angeles"},
        {"name": "Charlie", "city": "Chicago"},
        {"name": "David", "city": "New York"},
        {"name": "Eve", "city": "Los Angeles"}
    ]
    
    for contact in contacts:
        if contact["city"] == city:
            yield contact

if __name__ == '__main__':
    generator = contact_generator("New York")
    for _ in range(2):
        print(next(generator))