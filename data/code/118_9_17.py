import math

def multiply_numbers(numbers):
    if len(numbers) != 2:
        raise ValueError("The input list must contain exactly two elements.")
    return math.prod(numbers)

if __name__ == '__main__':
    sample_numbers = [15, 7]
    result = multiply_numbers(sample_numbers)
    print(result)