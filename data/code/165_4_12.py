import random

class ContactGenerator:
    def __init__(self, city, page_size=10):
        self.city = city
        self.page_size = page_size
        self.contacts = [
            {'name': f'Name{random.randint(1, 100)}', 'city': random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'])}
            for _ in range(1000)
        ]
    
    def get_next_page(self):
        filtered_contacts = (contact for contact in self.contacts if contact['city'] == self.city)
        page = [next(filtered_contacts) for _ in range(self.page_size)]
        return page

if __name__ == '__main__':
    generator = ContactGenerator("New York", 5)
    print(generator.get_next_page())
    print(generator.get_next_page())