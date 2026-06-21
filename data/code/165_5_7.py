import threading

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.lock = threading.Lock()
    
    def add_contact(self, name, number):
        with self.lock:
            if name not in self.contacts:
                self.contacts[name] = number
    
    def get_contact(self, name):
        with self.lock:
            return self.contacts.get(name, None)

if __name__ == '__main__':
    cb = ContactBook()
    sample_name = 'Bob'
    sample_number = '098-765-4321'
    cb.add_contact(sample_name, sample_number)
    print(f"Contact added: {cb.get_contact(sample_name)}")