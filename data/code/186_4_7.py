import math

def sort_numbers_with_nan(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")
    
    def is_nan(value):
        return math.isnan(value)
    
    return sorted(numbers, key=is_nan)

if __name__ == '__main__':
    sample_list = [3.14, 2.718, float('nan'), 1.618, float('nan')]
    result = sort_numbers_with_nan(sample_list)
    print(result)