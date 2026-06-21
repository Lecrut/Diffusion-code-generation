def generate_contacts(city, page_size=10):
    total_contacts = 1000000
    current_page = 0
    while True:
        start_index = current_page * page_size
        end_index = min((current_page + 1) * page_size, total_contacts)
        for i in range(start_index, end_index):
            contact = {'id': i, 'name': f'Contact {i}', 'city': city if i % 2 == 0 else 'Other City'}
            yield contact
        current_page += 1
        if end_index >= total_contacts:
            break
if __name__ == '__main__':
    city_filter = 'New York'
    page_size = 5
    generator = generate_contacts(city_filter, page_size)
    for _ in range(3):
        print(next(generator))