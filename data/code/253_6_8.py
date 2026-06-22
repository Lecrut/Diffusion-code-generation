def find_the_middle_value_among_three_convert_all(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_convert_all(3, 1, 2))
    print(find_the_middle_value_among_three_convert_all(5, 9, 7))
    print(find_the_middle_value_among_three_convert_all(-1, -3, -2))