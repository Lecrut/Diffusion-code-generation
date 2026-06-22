def find_the_middle_value_among_three_convert_all(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 20
    middle = find_the_middle_value_among_three_convert_all(num1, num2, num3)
    print(middle)