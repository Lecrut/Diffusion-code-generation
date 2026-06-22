import random

def random_from_tuple(t: tuple):
    if not t:
        return None
    return random.choice(t)

if __name__ == '__main__':
    sample_data = (10, 20, 30, 40, 50)
    result = random_from_tuple(sample_data)
    print(result)
    
    empty_data = ()
    empty_result = random_from_tuple(empty_data)
    print(empty_result)