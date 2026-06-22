def find_the_middle_value_among_three_summary(a, b, c):
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c

if __name__ == '__main__':
    print(find_the_middle_value_among_three_summary(10, 5, 20))
    print(find_the_middle_value_among_three_summary(10, 25, 15))
    print(find_the_middle_value_among_three_summary(3, 1, 2))