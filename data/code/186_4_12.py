import math

def sort_floats_with_nan(numbers):
    finite_numbers = []
    nan_values = []
    for num in numbers:
        if math.isnan(num):
            nan_values.append(num)
        else:
            finite_numbers.append(num)
    sorted_finite_numbers = sorted(finite_numbers)
    return sorted_finite_numbers + nan_values
if __name__ == '__main__':
    sample_values = [3.14, float('nan'), 2.718, float('nan'), 0.0, -1.0]
    result = sort_floats_with_nan(sample_values)
    print(result)