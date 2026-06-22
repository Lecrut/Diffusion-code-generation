import math

def find_min_value(numbers):
    if not numbers:
        return None
    min_val = float('inf')
    for num in numbers:
        if math.isnan(num):
            continue
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values = [3.14, 2.718, math.nan, 0.5, -1.5]
    print(find_min_value(sample_values))