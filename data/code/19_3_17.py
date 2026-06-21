import random
import functools

def fetch_random_tuple_element(collection):
    length = len(collection)
    if length == 0:
        return None
    index = random.randrange(length)
    return collection[index]

if __name__ == '__main__':
    sample_data = (55, 66, 77, 88, 99)
    empty_data = tuple()
    val1 = fetch_random_tuple_element(sample_data)
    val2 = fetch_random_tuple_element(empty_data)
    print(val1)
    print(val2)