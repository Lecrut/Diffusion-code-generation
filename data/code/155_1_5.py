from functools import reduce

def compute_total(numbers):
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = compute_total(sample_numbers)
    print(f"Total of {sample_numbers}: {result}")