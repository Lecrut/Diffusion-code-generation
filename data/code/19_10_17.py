import random

def _validate_list(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) == 0:
        raise ValueError("Input list cannot be empty")
    return data

def get_random_element(integers):
    _validate_list(integers)
    index = random.randint(0, len(integers) - 1)
    return integers[index]

if __name__ == '__main__':
    sample_values = [5, 15, 25, 35, 45, 55, 65, 75]
    selected = get_random_element(sample_values)
    print(selected)