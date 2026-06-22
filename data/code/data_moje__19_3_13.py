import random

def get_random_item(data):
    if not data:
        return None
    index = random.randint(0, len(data) - 1)
    return data[index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    empty_tuple = ()
    print(get_random_item(sample_tuple))
    print(get_random_item(empty_tuple))