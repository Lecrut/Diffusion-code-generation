import random

def get_random_item(t):
    if not t:
        return None
    return random.choice(t)

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    empty_tuple = ()
    print(get_random_item(sample_tuple))
    print(get_random_item(empty_tuple))