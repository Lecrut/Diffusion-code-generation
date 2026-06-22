def find_the_middle_value_among_three_convert_all(a, b, c):
    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c

if __name__ == '__main__':
    sample1 = find_the_middle_value_among_three_convert_all(10, 5, 20)
    print(sample1)
    sample2 = find_the_middle_value_among_three_convert_all(10, 5, 15)
    print(sample2)