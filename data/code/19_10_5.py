import random

def get_random_element(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return random.choice(numbers)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_random_element(sample_list)
    print(result)