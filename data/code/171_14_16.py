class StoreManager:
    def __init__(self):
        self._stores = []

    def add_store(self, name, description):
        if any(store['name'] == name for store in self._stores):
            return False
        self._stores.append({'name': name, 'description': description})
        return True

    def store_exists(self, name):
        return any(store['name'] == name for store in self._stores)

    def get_store_description(self, name):
        for store in self._stores:
            if store['name'] == name:
                return store['description']
        return None

if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store('Tech Innovations', 'A place for the latest tech gadgets.')
    manager.add_store('Book Haven', 'Your one-stop for all books.')
    print(manager.store_exists('Tech Innovations'))
    print(manager.get_store_description('Book Haven'))