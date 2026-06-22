def get_max_nested(nested_list):
    flattened = []
    stack = [iter(nested_list)]
    while stack:
        parent = stack[-1]
        try:
            item = next(parent)
            if isinstance(item, list):
                stack.append(iter(item))
            else:
                flattened.append(item)
        except StopIteration:
            stack.pop()
    if not flattened:
        raise ValueError("The nested list contains no numbers")
    return max(flattened)

if __name__ == '__main__':
    sample_data = [1, [2, 3, [4, 5]], 6, [[7], 8], 9]
    result = get_max_nested(sample_data)
    print(result)