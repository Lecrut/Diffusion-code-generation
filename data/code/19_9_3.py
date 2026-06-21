import random
from collections import namedtuple

def random_access_element(data_struct):
    index = random.randrange(len(data_struct))
    return data_struct[index]

if __name__ == '__main__':
    Person = namedtuple('Person', ['name', 'age', 'city'])
    sample_person = Person('Alice', 30, 'New York')
    result = random_access_element(sample_person)
    print(result)