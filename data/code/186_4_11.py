def sort_with_nan_at_end(numbers):
    return sorted(numbers, key=lambda x: (isinstance(x, float) and not math.isnan(x), x))

if __name__ == '__main__':
    import math
    sample_numbers = [3.14, 2.71, float('nan'), 0.0, -1.0, float('nan')]
    print(sort_with_nan_at_end(sample_numbers))