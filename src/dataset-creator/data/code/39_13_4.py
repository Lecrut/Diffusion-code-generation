import sys
def find_max_generator(iterable):
    max_val = -sys.maxsize
    for item in iterable:
        if isinstance(item, (int, float)):
            if item > max_val:
                max_val = item
    return max_val
if __name__ == '__main__':
    sample_data = [3.5, 7, 'apple', -10, None, True, 2]
    numeric_generator = (x for x in sample_data if isinstance(x, (int, float)))
    result = find_max_generator(numeric_generator)
    print(result)