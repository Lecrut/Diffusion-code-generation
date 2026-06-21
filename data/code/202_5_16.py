def flatten_and_find_largest(data):
    flattened = []
    for item in data:
        if isinstance(item, list):
            flattened.extend(flatten_and_find_largest(item))
        else:
            flattened.append(item)
    return max(flattened)

if __name__ == '__main__':
    sample_list = [12, 45, [67, 89], [34, [91]], 5]
    result = flatten_and_find_largest(sample_list)
    print(result)