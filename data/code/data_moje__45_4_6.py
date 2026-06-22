import sys

def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [34, 12, 56, 7, 89, 23, 45, 1, 99, 5]
    result = find_minimum(sample_data)
    print(result)