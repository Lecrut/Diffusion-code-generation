import threading

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.lock = threading.Lock()
    
    def _acquire_lock(self):
        return self.lock.acquire(blocking=True)
    
    def _release_lock(self):
        return self.lock.release()
    
    def add_contact(self, name, number):
        with self._acquire_lock():
            if name not in self.contacts:
                self.contacts[name] = number
    
    def get_contact(self, name):
        with self._acquire_lock():
            return self.contacts.get(name, None)

if __name__ == '__main__':
    cb = ContactBook()
    cb.add_contact('Alice', '123-456-7890')
    print(cb.get_contact('Alice'))