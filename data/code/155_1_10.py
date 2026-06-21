from functools import reduce

def calculate_total(numbers):
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_numbers = [10, 23, 45, 67, 89]
    result = calculate_total(sample_numbers)
    print(f"Total of {sample_numbers}: {result}")