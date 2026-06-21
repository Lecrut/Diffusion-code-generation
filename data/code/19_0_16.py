import random

def get_random_element(lst):
    return lst[random.randrange(len(lst))]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_random_element(sample_list))