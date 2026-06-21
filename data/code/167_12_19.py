from collections import namedtuple

StoreInfo = namedtuple('StoreInfo', ['name', 'age'])

if __name__ == '__main__':
    store1 = StoreInfo(name='ABC Store', age=25)
    store2 = StoreInfo(name='XYZ Shop', age=30)

    print(store1.name, store1.age)
    print(store2.name, store2.age)