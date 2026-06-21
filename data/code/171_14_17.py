class StoreManager:
    MAX_STORES = 100
    
    def __init__(self):
        self._stores = []
    
    @staticmethod
    def _is_valid_name(name):
        return isinstance(name, str) and len(name.strip()) > 0
    
    def add_store(self, name, description):
        if not self._is_valid_name(name):
            raise ValueError("Invalid store name")
        if len(self._stores) >= self.MAX_STORES:
            raise Exception("Store limit reached")
        if any(store['name'] == name for store in self._stores):
            raise Exception("Store already exists")
        self._stores.append({'name': name, 'description': description})
    
    def store_exists(self, name):
        return any((store['name'] == name for store in self._stores))
    
    def get_store_description(self, name):
        for store in self._stores:
            if store['name'] == name:
                return store['description']
        return None

if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store('Tech Innovations', 'A place for the latest tech gadgets.')
    print(manager.store_exists('Tech Innovations'))
    print(manager.get_store_description('Tech Innovations'))