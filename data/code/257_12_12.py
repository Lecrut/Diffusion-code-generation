import sys

def calculate_difference(numbers):
    if not numbers:
        return None
    min_num = min(numbers)
    max_num = max(numbers)
    return abs(max_num - min_num)

if __name__ == '__main__':
    sample_values = (3.5, 1.2, 7.8, 4.9)
    result = calculate_difference(sample_values)
    print(result)