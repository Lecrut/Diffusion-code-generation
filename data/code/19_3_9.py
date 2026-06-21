import random

def get_random_from_tuple(data_tuple):
    if not data_tuple:
        return None
    return random.choice(data_tuple)

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = get_random_from_tuple(sample_tuple)
    print(result)
    
    empty_tuple = ()
    empty_result = get_random_from_tuple(empty_tuple)
    print(empty_result)