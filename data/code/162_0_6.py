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
    kv_store.set('key1', 'value1')
    print(kv_store.get('key1'))
    kv_store.delete('key1')
    print(kv_store.get('key1'))