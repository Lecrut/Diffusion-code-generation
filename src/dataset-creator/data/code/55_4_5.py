def swap_neighboring_elements(arr):
    if len(arr) < 2:
        return arr
    def is_nested(item):
        return isinstance(item, (list, tuple)) and not isinstance(item, str)
    for i in range(len(arr) - 1):
        current = arr[i]
        next_item = arr[i + 1]
        if is_nested(current) and is_nested(next_item) and len(current) == len(next_item):
            temp = arr[i:i+2]
            arr[i], arr[i+1] = next_item, current
    return arr
if __name__ == '__main__':
    sample_data = [30, 45, 'a', ['x', 'y'], (1, 2), ('b', 'c')]
    working_copy = list(sample_data)
    result = swap_neighboring_elements(working_copy)
    print(result)