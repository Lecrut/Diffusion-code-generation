def find_the_middle_value_among_three_transform(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    sample_values = {1: 5, 2: 3, 3: 9}
    middle_value = find_the_middle_value_among_three_transform(**sample_values)
    print(middle_value)