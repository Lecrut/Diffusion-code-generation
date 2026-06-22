def find_the_middle_value_among_three_filter_valid(a, b, c):
    if a > b:
        if b > c:
            return b
        else:
            return c
    elif a < b:
        if a > c:
            return a
        else:
            return c
    else:
        return a

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 15
    middle_value = find_the_middle_value_among_three_filter_valid(num1, num2, num3)
    print(middle_value)