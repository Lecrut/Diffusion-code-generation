from collections import namedtuple
StoreInfo = namedtuple('StoreInfo', ['name', 'age'])
if __name__ == '__main__':
    store1 = StoreInfo(name='ABC Store', age=20)
    print(store1.name)
    print(store1.age)