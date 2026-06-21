import random

def get_random_from_tuple(data):
    if not data:
        return None
    return random.choice(data)

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    empty_tuple = ()
    result = get_random_from_tuple(sample_tuple)
    print(result)
    empty_result = get_random_from_tuple(empty_tuple)
    print(empty_result)