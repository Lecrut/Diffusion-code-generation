def find_largest_value(values):
    if not values:
        return None
    largest = values[0]
    for number in values[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data = [3, 7, 2, 9, 1, 15, 4, 8, 12]
    result = find_largest_value(sample_data)
    print(result)