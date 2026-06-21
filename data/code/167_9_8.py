class StoreRecord:
    def __init__(self):
        self.store_name = "MainStore"
        self.age = 10

    def get_record(self):
        return {
            'store_name': self.store_name,
            'age': self.age
        }

if __name__ == '__main__':
    store = StoreRecord()
    print(store.get_record())