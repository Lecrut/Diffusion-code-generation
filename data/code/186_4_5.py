def sort_floats_with_nan(numbers):
    return sorted(numbers, key=lambda x: (isinstance(x, float) and not isinstance(x, int), x))

if __name__ == '__main__':
    sample_values = [3.14, 2.71, float('nan'), 0.0, -1.0, float('inf')]
    print(sort_floats_with_nan(sample_values))