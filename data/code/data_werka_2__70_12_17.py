def extract_boundary_items(data):
    if len(data) == 0:
        raise ValueError("Sequence cannot be empty")
    return data[0], data[len(data) - 1]

if __name__ == '__main__':
    values = [7, 3, 9, 1, 5]
    start, end = extract_boundary_items(values)
    print(start, end)