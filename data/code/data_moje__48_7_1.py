def find_max(nested_list):
    stack = [iter(nested_list)]
    max_value = None
    while stack:
        current_iter = stack[-1]
        try:
            item = next(current_iter)
            if isinstance(item, list):
                stack.append(iter(item))
            else:
                if max_value is None or item > max_value:
                    max_value = item
        except StopIteration:
            stack.pop()
    return max_value

if __name__ == '__main__':
    data = [1, [2, [3, 4], 5], [6, [7, 8]], 9]
    result = find_max(data)
    print(result)