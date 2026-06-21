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

def filter_and_paginate(generator, page_size=10):
    filtered_contacts = (contact for contact in generator)
    while True:
        page = [next(filtered_contacts) for _ in range(page_size)]
        if not page:
            break
        yield page

if __name__ == '__main__':
    contacts_generator = contact_generator("New York")
    filtered_paginated_contacts = filter_and_paginate(contacts_generator, 2)
    for page in filtered_paginated_contacts:
        print(page)