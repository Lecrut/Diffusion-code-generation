class StoreRecord:
    def __init__(self):
        self.store_name = 'StoreX'
        self.age = 35

    def get_record(self):
        return {'store_name': self.store_name, 'age': self.age}

if __name__ == '__main__':
    store_record = StoreRecord()
    print(store_record.get_record())