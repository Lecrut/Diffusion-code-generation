import math

def min_value(numbers):
    if not numbers:
        return None
    min_val = math.inf
    for num in numbers:
        if not math.isnan(num) and num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_values = [3.14, 2.71, float('nan'), 0.0, -1.0]
    print(min_value(sample_values))