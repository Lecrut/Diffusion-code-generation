def flatten_and_find_max(nested_list):
    flat = []
    stack = [nested_list]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current)
        else:
            flat.append(current)
    return max(flat)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, 6]], 7]
    result = flatten_and_find_max(sample_data)
    print(result)