import math

def sort_with_nan(numbers):
    return sorted(numbers, key=lambda x: (math.isnan(x), x))

if __name__ == '__main__':
    sample_values = [3.5, 1.2, float('nan'), 4.8, float('nan'), 2.1]
    print(sort_with_nan(sample_values))