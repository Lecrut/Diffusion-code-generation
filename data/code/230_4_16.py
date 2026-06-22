import itertools

def calculate_running_total(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the tuple must be numbers")
    return tuple(itertools.accumulate(numbers))

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40)
    result = calculate_running_total(sample_numbers)
    print(result)