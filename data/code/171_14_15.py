class StoreManager:

    def __init__(self):
        self._stores = []

    def add_store(self, name, description):
        if not any((store['name'] == name for store in self._stores)):
            self._stores.append({'name': name, 'description': description})

    def store_exists(self, name):
        return any((store['name'] == name for store in self._stores))

    def get_store_description(self, name):
        store = next((store for store in self._stores if store['name'] == name), None)
        return store['description'] if store else None
if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store('Store A', 'Description of Store A')
    manager.add_store('Store B', 'Description of Store B')
    print(manager.store_exists('Store A'))
    print(manager.store_exists('Store C'))
    print(manager.get_store_description('Store A'))
    print(manager.get_store_description('Store C'))