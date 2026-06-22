import random

def get_random_element(input_list):
    return random.choice(input_list)

if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    result = get_random_element(numbers)
    print(result)