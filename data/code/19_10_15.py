import random

def get_random_element(lst):
    if not lst:
        raise ValueError("Cannot select from an empty list")
    return random.choice(lst)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = get_random_element(sample_list)
    print(result)