def find_the_middle_value_among_three_convert_all(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_convert_all(5, 3, 9))
    print(find_the_middle_value_among_three_convert_all(10, -2, 7))
    print(find_the_middle_value_among_three_convert_all(4, 4, 4))