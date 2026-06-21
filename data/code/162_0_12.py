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
    kvs = KeyValueStore()
    kvs.set('a', 1)
    print(kvs.get('a'))
    kvs.delete('a')
    print(kvs.get('a'))