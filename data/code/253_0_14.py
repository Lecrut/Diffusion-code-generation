def find_the_middle_value_among_three_transform(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_transform(5, 3, 9))
    print(find_the_middle_value_among_three_transform(3, 1, 2))