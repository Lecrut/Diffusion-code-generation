import random

def get_random_value_from_range(start, stop, step, values):
    if not values:
        raise IndexError("Cannot select from an empty list")
    
    indices_count = len(values)
    random_index = random.randint(0, indices_count - 1)
    
    return values[random_index]

if __name__ == '__main__':
    start = 1
    stop = 100
    step = 2
    pre_defined_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    result = get_random_value_from_range(start, stop, step, pre_defined_values)
    print(result)