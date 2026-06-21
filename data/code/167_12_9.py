from collections import namedtuple

StoreInfo = namedtuple('StoreInfo', ['name', 'age'])

class StoreManager:
    def __init__(self):
        self.stores = [
            StoreInfo(name='ABC Store', age=5),
            StoreInfo(name='XYZ Market', age=3)
        ]

    @staticmethod
    def create_store_info(name, age):
        return StoreInfo(name=name, age=age)

if __name__ == '__main__':
    manager = StoreManager()
    for store in manager.stores:
        print(store.name, store.age)

    new_store = StoreManager.create_store_info('New Store', 10)
    print(new_store.name, new_store.age)