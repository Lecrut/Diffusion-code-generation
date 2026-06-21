import math

def sort_floats_with_nan(numbers):
    return sorted(numbers, key=lambda x: (math.isnan(x), x))

if __name__ == '__main__':
    sample_values = [3.14, 2.71, float('nan'), 0.0, -1.618]
    print(sort_floats_with_nan(sample_values))