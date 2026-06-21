class KeyValueStore:
    def __init__(self):
        self.store = {}
    
    def set(self, key, value):
        self.store[key] = value
    
    def get(self, key):
        return self.store.get(key)
    
    def delete(self, key):
        if key in self.store:
            del self.store[key]

if __name__ == '__main__':
    kv_store = KeyValueStore()
    kv_store.set('test_key', 'test_value')
    print(kv_store.get('test_key'))
    kv_store.delete('test_key')
    print(kv_store.get('test_key'))