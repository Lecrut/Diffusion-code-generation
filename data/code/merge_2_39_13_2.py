import sys
def find_max_generator(values):
    max_val = -sys.maxsize
    for val in values:
        if isinstance(val, (int, float)) and not isinstance(val, bool) and val > max_val:
            max_val = val
    return max_val
if __name__ == '__main__':
    sample_data = [10.5, 23, -45, 'hello', None, True, 789]
    numeric_data = [x for x in sample_data if isinstance(x, (int, float)) and not isinstance(x, bool)]
    result = -sys.maxsize
    try:
        max_val = numeric_data[0]
        iterator = (x for x in numeric_data)
        max_val = next(iterator) if numeric_data else None
        for val in iterator:
            if val > max_val:
                max_val = val
    except ValueError:
        result = "No valid numbers found"
    print(result)