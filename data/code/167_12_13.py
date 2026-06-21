from collections import namedtuple

Store = namedtuple('Store', ['name', 'age'])

if __name__ == '__main__':
    store1 = Store(name='Central Market', age=50)
    store2 = Store(name='Fresh Breeze', age=30)

    print(store1.name, store1.age)
    print(store2.name, store2.age)