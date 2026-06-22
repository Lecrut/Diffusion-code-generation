import random

def get_random_item(data_tuple):
    if len(data_tuple) == 0:
        return None
    return random.choice(data_tuple)

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    empty_tuple = ()
    
    result_1 = get_random_item(sample_tuple)
    result_2 = get_random_item(empty_tuple)
    
    print(result_1)
    print(result_2)