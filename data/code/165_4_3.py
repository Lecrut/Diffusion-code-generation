import random

def generate_contacts(num_contacts):
    for _ in range(num_contacts):
        yield {
            'name': f'Name{random.randint(1, 100)}',
            'city': random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'])
        }

def filter_and_paginate_contacts(generator, city, page_size=10):
    filtered_contacts = (contact for contact in generator if contact['city'] == city)
    while True:
        page = [next(filtered_contacts) for _ in range(page_size)]
        if not page:
            break
        yield page

if __name__ == '__main__':
    contacts_generator = generate_contacts(100)
    filtered_paginated_contacts = filter_and_paginate_contacts(contacts_generator, 'New York', 5)
    
    for page in filtered_paginated_contacts:
        print(page)