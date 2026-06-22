def flatten_and_find_max(nested_list):
    flat_list = []
    stack = [nested_list]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in reversed(current):
                stack.append(item)
        else:
            flat_list.append(current)
    return max(flat_list) if flat_list else None

if __name__ == '__main__':
    sample_data = [1, [2, [3, 4], 5], [6, [7, [8, 9]]], 10]
    result = flatten_and_find_max(sample_data)
    print(result)