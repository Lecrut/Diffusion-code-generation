def find_the_middle_value_among_three_convert_all(a, b, c):
    sorted_values = sorted([a, b, c])
    return sorted_values[1]

if __name__ == '__main__':
    num1 = 30
    num2 = 15
    num3 = 25
    middle_value = find_the_middle_value_among_three_convert_all(num1, num2, num3)
    print(middle_value)