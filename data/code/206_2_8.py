def find_lowest_value(values):
    if not values:
        raise ValueError("List cannot be empty")
    lowest = values[0]
    for value in values[1:]:
        if value < lowest:
            lowest = value
    return lowest

if __name__ == '__main__':
    sample_data = [3.14, 1.618, 2.718, -0.5, 9.99]
    try:
        print(find_lowest_value(sample_data))
    except ValueError as e:
        print(e)