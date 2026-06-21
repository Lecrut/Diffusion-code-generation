import math

def sort_floats_with_nan(numbers):
    finite_numbers = [num for num in numbers if not math.isnan(num)]
    nan_count = len([num for num in numbers if math.isnan(num)])
    sorted_finite_numbers = sorted(finite_numbers)
    return sorted_finite_numbers + [math.nan] * nan_count

if __name__ == '__main__':
    sample_list = [3.14, 2.71, float('nan'), 0.0, -1.618, float('nan')]
    result = sort_floats_with_nan(sample_list)
    print(result)