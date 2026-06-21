from functools import reduce

def compute_total(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(compute_total(sample_numbers))