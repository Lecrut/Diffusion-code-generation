import random

def get_random_tuple_item(data):
    if not data:
        return None
    return random.choice(data)

if __name__ == '__main__':
    sample_data = (10, 20, 30, 40, 50)
    empty_data = ()
    print(get_random_tuple_item(sample_data))
    print(get_random_tuple_item(empty_data))