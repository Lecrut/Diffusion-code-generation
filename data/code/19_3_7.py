import random

def get_random_item(t):
    if len(t) == 0:
        return None
    return random.choice(t)

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    empty_tuple = ()
    result1 = get_random_item(sample_tuple)
    result2 = get_random_item(empty_tuple)
    print(result1)
    print(result2)