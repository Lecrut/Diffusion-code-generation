def find_minimum(values):
    min_value = values[0]
    for value in values:
        if value < min_value:
            min_value = value
    return min_value

if __name__ == '__main__':
    sample_values = [7, 4, 2, 8, 1, 5]
    minimum_value = find_minimum(sample_values)
    print(minimum_value)