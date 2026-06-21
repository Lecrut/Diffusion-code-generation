def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def check_item_in_nested_list(data, value):
    flat_data = flatten_list(data)
    return value in flat_data

if __name__ == '__main__':
    sample_list = [
        [1, 2, [3, 4]],
        [5, 6],
        [7, 8, 9]
    ]
    value_to_find = 4
    result1 = check_item_in_nested_list(sample_list, value_to_find)
    print(f"Checking for '{value_to_find}': {result1}")
    value_to_find = 10
    result2 = check_item_in_nested_list(sample_list, value_to_find)
    print(f"Checking for '{value_to_find}': {result2}")