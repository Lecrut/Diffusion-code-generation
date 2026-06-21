from functools import reduce

def find_min(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    return reduce(lambda x, y: x if x < y else y, numbers)

if __name__ == '__main__':
    sample_values = [10, 5, 23, 8, 1]
    print(find_min(sample_values))