import random

def get_random_item(data):
    if not data:
        return None
    return random.choice(data)

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = get_random_item(sample_tuple)
    print(result)
    empty_tuple = ()
    empty_result = get_random_item(empty_tuple)
    print(empty_result)