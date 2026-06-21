from collections import namedtuple

StoreInfo = namedtuple('StoreInfo', ['name', 'age'])

if __name__ == '__main__':
    store1 = StoreInfo(name='ABC Store', age=5)
    store2 = StoreInfo(name='XYZ Market', age=3)
    print(f"Store: {store1.name}, Age: {store1.age}")
    print(f"Store: {store2.name}, Age: {store2.age}")