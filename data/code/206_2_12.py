def locate_smallest_value(floats):
    if not floats:
        raise ValueError("Input list cannot be empty")
    lowest = floats[0]
    for value in floats[1:]:
        if value < lowest:
            lowest = value
    return lowest

if __name__ == '__main__':
    test_data = [5.67, 2.34, -1.23, 0.0, 9.87]
    try:
        print(locate_smallest_value(test_data))
    except ValueError as e:
        print(e)