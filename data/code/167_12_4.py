from collections import namedtuple

StoreInfo = namedtuple('StoreInfo', ['name', 'age'])

if __name__ == '__main__':
    store1 = StoreInfo(name='Central Market', age=30)
    store2 = StoreInfo(name='Green Grocer', age=25)

    print(f"Store Name: {store1.name}, Age: {store1.age}")
    print(f"Store Name: {store2.name}, Age: {store2.age}")