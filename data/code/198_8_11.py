def find_smallest(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    return data[0]
if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9]
    try:
        smallest_item = find_smallest(sample_data)
        print(smallest_item)
    except ValueError as e:
        print(e)