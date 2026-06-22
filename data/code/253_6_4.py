def find_the_middle_value_among_three_convert_all(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_convert_all(5, 3, 8))
    print(find_the_middle_value_among_three_convert_all(10, 20, 15))
    print(find_the_middle_value_among_three_convert_all(-1, -5, -3))