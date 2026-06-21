import random
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])

def random_access_namedtuple(instance):
    index = random.randint(0, len(instance) - 1)
    return instance[index]

if __name__ == '__main__':
    sample_person = Person('Alice', 30, 'Wonderland')
    result = random_access_namedtuple(sample_person)
    print(result)