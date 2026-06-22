import itertools

def calculate_running_total(numbers_tuple):
    return tuple(itertools.accumulate(numbers_tuple))

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    result = calculate_running_total(sample_numbers)
    print(result)