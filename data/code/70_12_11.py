def extract_boundary_values(data):
    if not isinstance(data, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(data) == 0:
        raise ValueError("Sequence cannot be empty")
    return data[0], data[-1]

if __name__ == '__main__':
    values = [42, 99, 15, 88, 3]
    first_item, last_item = extract_boundary_values(values)
    print(first_item, last_item)