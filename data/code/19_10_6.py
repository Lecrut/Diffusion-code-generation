import random

NUMBERS = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def get_random_element(input_list):
    if not input_list:
        raise ValueError("List cannot be empty")
    index = random.randrange(len(input_list))
    return input_list[index]

if __name__ == '__main__':
    sample_data = NUMBERS
    result = get_random_element(sample_data)
    print(result)