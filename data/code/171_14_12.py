class StoreManager:
    _stores = []

    @staticmethod
    def add_store(name, description):
        if not any((store['name'] == name for store in StoreManager._stores)):
            StoreManager._stores.append({'name': name, 'description': description})

    @staticmethod
    def store_exists(name):
        return any((store['name'] == name for store in StoreManager._stores))

    @staticmethod
    def get_store_description(name):
        for store in StoreManager._stores:
            if store['name'] == name:
                return store['description']
        return None

if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store('Tech Innovations', 'A place for the latest tech gadgets.')
    manager.add_store('Book Haven', 'Your one-stop for all books.')
    print(manager.store_exists('Tech Innovations'))
    print(manager.get_store_description('Book Haven'))