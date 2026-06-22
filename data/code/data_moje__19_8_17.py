import random

def get_random_value_from_list(int_list):
    if not int_list:
        return None
    index = random.randrange(len(int_list))
    return int_list[index]

if __name__ == '__main__':
    sample_numbers = [10, 25, 42, 67, 89, 33, 15]
    result = get_random_value_from_list(sample_numbers)
    print(result)