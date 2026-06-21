class KeyValueStore:
    def __init__(self):
        self.store = {}
    
    def set(self, key, value):
        if not isinstance(key, str) or not isinstance(value, str):
            raise ValueError("Both key and value must be strings")
        self.store[key] = value
    
    def get(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        return self.store.get(key, None)
    
    def delete(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        if key in self.store:
            del self.store[key]

if __name__ == '__main__':
    kv_store = KeyValueStore()
    kv_store.set('new_key', 'new_value')
    print(kv_store.get('new_key'))
    kv_store.delete('new_key')
    print(kv_store.get('new_key'))