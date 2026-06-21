import random

def get_random_item(tuple_data):
    if not tuple_data:
        return None
    return random.choice(tuple_data)

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    empty_tuple = ()
    result1 = get_random_item(sample_tuple)
    result2 = get_random_item(empty_tuple)
    print(result1)
    print(result2)