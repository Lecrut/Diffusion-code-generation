class StoreRecord:
    STORE_NAME = "HardcodedStore"
    AGE = 10

    def get_record(self):
        return {
            'store_name': self.STORE_NAME,
            'age': self.AGE
        }

if __name__ == '__main__':
    store_record = StoreRecord()
    print(store_record.get_record())