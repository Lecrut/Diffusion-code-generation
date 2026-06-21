class StoreRecord:
    def __init__(self):
        self.store_name = "Central Market"
        self.age = 50

    def get_record(self):
        return {
            'store_name': self.store_name,
            'age': self.age
        }

if __name__ == '__main__':
    store_record = StoreRecord()
    print(store_record.get_record())