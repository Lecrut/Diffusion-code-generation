class StoreManager:
    def __init__(self):
        self._stores = []

    def add_store(self, name, description):
        if not isinstance(name, str) or not isinstance(description, str):
            raise ValueError("Both name and description must be strings.")
        if any((store['name'] == name for store in self._stores)):
            raise ValueError(f"Store '{name}' already exists.")
        self._stores.append({'name': name, 'description': description})

    def store_exists(self, name):
        return any((store['name'] == name for store in self._stores))

    def get_store_description(self, name):
        for store in self._stores:
            if store['name'] == name:
                return store['description']
        raise KeyError(f"Store '{name}' not found.")

if __name__ == '__main__':
    manager = StoreManager()
    try:
        manager.add_store('Tech Innovations', 'A place for the latest tech gadgets.')
        manager.add_store('Book Haven', 'Your one-stop for all books.')
        print(manager.store_exists('Tech Innovations'))
        print(manager.get_store_description('Book Haven'))
    except ValueError as e:
        print(f"Value Error: {e}")
    except KeyError as e:
        print(f"Key Error: {e}")