from collections import namedtuple

StoreData = namedtuple('StoreData', ['name', 'age'])

if __name__ == '__main__':
    store1 = StoreData(name='Tech Hub', age=20)
    store2 = StoreData(name='Green Grocer', age=35)
    
    print(f"Store: {store1.name}, Age: {store1.age}")
    print(f"Store: {store2.name}, Age: {store2.age}")