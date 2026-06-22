import random

def get_random_item(input_tuple):
    if not input_tuple:
        return None
    return random.choice(input_tuple)

if __name__ == '__main__':
    sample_data = (10, 20, 30, 40, 50)
    result = get_random_item(sample_data)
    print(result)
    empty_data = ()
    empty_result = get_random_item(empty_data)
    print(empty_result)