from collections import namedtuple

Store = namedtuple('Store', ['name', 'age'])

if __name__ == '__main__':
    store1 = Store(name='ABC Store', age=25)
    print(store1.name)
    print(store1.age)