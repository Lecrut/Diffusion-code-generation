def find_the_middle_value_among_three_filter_valid(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 15
    middle = find_the_middle_value_among_three_filter_valid(num1, num2, num3)
    print(middle)