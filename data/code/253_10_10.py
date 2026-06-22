def find_the_middle_value_among_three_calculate(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c

if __name__ == '__main__':
    print(find_the_middle_value_among_three_calculate(1, 2, 3))
    print(find_the_middle_value_among_three_calculate(5, 1, 4))
    print(find_the_middle_value_among_three_calculate(10, 20, 30))
    print(find_the_middle_value_among_three_calculate(1, 100, 50))
    print(find_the_middle_value_among_three_calculate(-5, 0, 5))
    print(find_the_middle_value_among_three_calculate(-10, -5, -20))