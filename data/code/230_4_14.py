import itertools

def calculate_running_total(numbers):
    return tuple(itertools.accumulate(numbers))

if __name__ == '__main__':
    sample_numbers = (1, 2, 3, 4, 5)
    result = calculate_running_total(sample_numbers)
    print(result)