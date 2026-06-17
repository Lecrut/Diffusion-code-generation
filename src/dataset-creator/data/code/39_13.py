import sys
def find_max_generator(iterable):
    max_val = -sys.maxsize
    for item in iterable:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            if item > max_val:
                max_val = item
    return max_val
if __name__ == '__main__':
    data = [3.5, 7, 'apple', None, -2, True, 10]
    filtered_data = (x for x in data if isinstance(x, (int, float)) and not isinstance(x, bool) and x is not None)
    result = find_max_generator(filtered_data)
    print(result)