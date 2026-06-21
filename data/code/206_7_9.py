def find_min_ascii(values):
    if not values:
        return None
    min_value = values[0]
    for value in values[1:]:
        if value < min_value:
            min_value = value
    return min_value

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    print("Minimum ASCII value:", find_min_ascii(sample_list))