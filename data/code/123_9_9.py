from functools import reduce

def sum_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be numbers")
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(sum_numbers(sample_values))