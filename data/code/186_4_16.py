import math

NAN_SORT_KEY = (math.inf, False)

def sort_floats_with_nan(nums):
    return sorted(nums, key=lambda x: (isinstance(x, float) and math.isnan(x), x))

if __name__ == '__main__':
    sample_values = [3.14, 2.71, float('nan'), 0.0, -1.618]
    result = sort_floats_with_nan(sample_values)
    print(result)