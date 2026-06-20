from functools import reduce

def sum_numbers(numbers):
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements in the list must be numbers")
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = sum_numbers(sample_values)
    print(result)