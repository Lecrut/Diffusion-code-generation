def flatten_and_find_max(nested_list):
    max_value = None
    stack = [nested_list]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in reversed(current):
                stack.append(item)
        else:
            if max_value is None or current > max_value:
                max_value = current
    return max_value

if __name__ == '__main__':
    data = [1, [2, 3, [4, 5]], 6, [7, [8, 9, [10]]]]
    print(flatten_and_find_max(data))