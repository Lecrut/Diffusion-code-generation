def extract_boundaries(items):
    if not isinstance(items, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(items) == 0:
        raise ValueError("Sequence must not be empty")
    if len(items) == 1:
        return items[0], items[0]
    return items[0], items[-1]

if __name__ == '__main__':
    data_set = [42, 87, 19, 63, 21]
    first_item, last_item = extract_boundaries(data_set)
    print(first_item, last_item)