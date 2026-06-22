def find_the_middle_value_among_three_transform(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    middle_value = find_the_middle_value_among_three_transform(4, 7, 2)
    print(middle_value)