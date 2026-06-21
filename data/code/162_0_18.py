class KeyValueStore:
    def __init__(self):
        self.store = {}
    
    def validate_key(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
    
    def set(self, key, value):
        self.validate_key(key)
        self.store[key] = value
    
    def get(self, key):
        self.validate_key(key)
        return self.store.get(key, None)
    
    def delete(self, key):
        self.validate_key(key)
        if key in self.store:
            del self.store[key]

if __name__ == '__main__':
    kv_store = KeyValueStore()
    kv_store.set('test_key', 'test_value')
    print(kv_store.get('test_key'))
    kv_store.delete('test_key')
    print(kv_store.get('test_key'))