import random

NUM_CONTACTS = 1000
CITIES = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

def generate_contacts(num_contacts):
    for _ in range(num_contacts):
        yield {'name': f'Name{random.randint(1, 100)}', 'city': random.choice(CITIES)}

class ContactFilter:
    def __init__(self, city, page_size=10):
        self.city = city
        self.page_size = page_size
        self.contact_generator = generate_contacts(NUM_CONTACTS)
    
    def get_next_page(self):
        page = []
        while len(page) < self.page_size:
            try:
                contact = next(self.contact_generator)
                if contact['city'] == self.city:
                    page.append(contact)
            except StopIteration:
                break
        return page

if __name__ == '__main__':
    filter_instance = ContactFilter('New York', 5)
    for _ in range(2):
        print(filter_instance.get_next_page())