MAX_VALUE = float('inf')

def flatten_and_find_max(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_and_find_max(item))
        else:
            flattened_list.append(item)
    return max(flattened_list, default=MAX_VALUE)
if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]]]
    result = flatten_and_find_max(sample_list)
    print(result)
    sample_list_2 = [[10, 20], 30, [40, [50, 60]]]
    result_2 = flatten_and_find_max(sample_list_2)
    print(result_2)