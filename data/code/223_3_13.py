from functools import reduce

def find_max(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(find_max(sample_numbers))