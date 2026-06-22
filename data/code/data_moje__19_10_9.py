import random

def get_random_element(numbers):
    return random.choice(numbers)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_random_element(sample_list)
    print(result)