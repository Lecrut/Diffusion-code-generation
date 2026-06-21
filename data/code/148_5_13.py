def find_greatest_element(values):
    if not values:
        return None
    greatest = values[0]
    for value in values[1:]:
        if value > greatest:
            greatest = value
    return greatest

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_greatest_element(sample_values)
    print(result)