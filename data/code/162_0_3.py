class KeyValueStore:
    def __init__(self):
        self.store = {}
    
    def set(self, key, value):
        self.store[key] = value
    
    def get(self, key):
        return self.store.get(key, None)
    
    def delete(self, key):
        if key in self.store:
            del self.store[key]

if __name__ == '__main__':
    kv_store = KeyValueStore()
    kv_store.set('example_key', 'example_value')
    print(kv_store.get('example_key'))
    kv_store.delete('example_key')
    print(kv_store.get('example_key'))