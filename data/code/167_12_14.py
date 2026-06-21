from collections import namedtuple

StoreInfo = namedtuple('StoreInfo', ['name', 'age'])

if __name__ == '__main__':
    store1 = StoreInfo(name='Central Market', age=30)
    store2 = StoreInfo(name='Fresh Breeze', age=25)

    print(store1.name, store1.age)
    print(store2.name, store2.age)