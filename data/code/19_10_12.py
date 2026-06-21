import random

def get_random_element(lst):
    return random.choice(lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_random_element(sample_list)
    print(result)