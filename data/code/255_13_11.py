def find_max_value(lst):
    max_val = float('-inf')
    for item in lst:
        if isinstance(item, list):
            max_val = max(max_val, find_max_value(item))
        else:
            max_val = max(max_val, item)
    return max_val
if __name__ == '__main__':
    sample_list = [1, 2, [3, 4, [5, 6], 7], 8]
    print(find_max_value(sample_list))