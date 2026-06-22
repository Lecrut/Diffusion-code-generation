def find_lowest(values):
    if not values:
        return None
    lowest = values[0]
    for val in values:
        if val < lowest:
            lowest = val
    return lowest

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.61, 4.50, 0.99]
    result = find_lowest(sample_values)
    print(result)