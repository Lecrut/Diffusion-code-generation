import random

def get_random_element(items):
    return items[random.randint(0, len(items) - 1)]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_random_element(sample_list))