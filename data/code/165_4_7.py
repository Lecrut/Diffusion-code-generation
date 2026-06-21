def contact_generator(city, page_size=10):
    contacts = [
        {"name": "Alice", "city": "New York"},
        {"name": "Bob", "city": "Los Angeles"},
        {"name": "Charlie", "city": "Chicago"},
        {"name": "David", "city": "New York"},
        {"name": "Eve", "city": "Los Angeles"}
    ]
    filtered_contacts = [contact for contact in contacts if contact["city"] == city]
    total_pages = (len(filtered_contacts) + page_size - 1) // page_size
    current_page = 0

    while current_page < total_pages:
        start_index = current_page * page_size
        end_index = min(start_index + page_size, len(filtered_contacts))
        yield filtered_contacts[start_index:end_index]
        current_page += 1

if __name__ == '__main__':
    gen = contact_generator("New York", 2)
    for page in gen:
        print(page)