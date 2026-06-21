def is_valid_nested_list(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    for item in data:
        if isinstance(item, list):
            if not is_valid_nested_list(item):
                return False
        elif not isinstance(item, (int, float)):
            raise ValueError("List items must be integers or floats")
    return True

def flatten_and_find_largest(data):
    flattened = []
    def flatten(sub_data):
        for item in sub_data:
            if isinstance(item, list):
                flatten(item)
            else:
                flattened.append(item)
    flatten(data)
    if not flattened:
        raise ValueError("Input list cannot be empty after flattening")
    largest = flattened[0]
    for number in flattened[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [12, 45, [67, 89], 34, 91, [5]]
    is_valid_nested_list(sample_list)
    result = flatten_and_find_largest(sample_list)
    print(result)