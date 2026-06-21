import random

def get_random_item(data_tuple):
    if not data_tuple:
        return None
    return random.choice(data_tuple)

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result1 = get_random_item(sample_tuple)
    print(result1)
    empty_tuple = ()
    result2 = get_random_item(empty_tuple)
    print(result2)