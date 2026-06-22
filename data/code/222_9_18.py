def locate_smallest_value(data):
    if not data:
        raise ValueError('Data must be non-empty')
    smallest = data[0]
    for value in data[1:]:
        if value < smallest:
            smallest = value
    return smallest
if __name__ == '__main__':
    dataset1 = [5, 2, 8, 1, 9]
    dataset2 = (100, 45, 33, 99)
    empty_data = []
    single_entry = [42]
    try:
        print(f'Smallest in {dataset1}: {locate_smallest_value(dataset1)}')
        print(f'Smallest in {dataset2}: {locate_smallest_value(dataset2)}')
        locate_smallest_value(empty_data)
    except ValueError as e:
        print(e)