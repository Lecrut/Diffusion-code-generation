def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[0]

if __name__ == '__main__':
    sample_values = [5, 2, 8, 1]
    try:
        smallest_item = find_smallest(sample_values)
        print(smallest_item)
    except ValueError as e:
        print(e)