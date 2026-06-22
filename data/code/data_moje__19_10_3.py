import random

def get_random_element(int_list):
    if not int_list:
        raise ValueError("List cannot be empty")
    return random.choice(int_list)

if __name__ == '__main__':
    sample_list = [10, 25, 30, 45, 60, 75, 90]
    result = get_random_element(sample_list)
    print(result)