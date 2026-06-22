def sort_three_numbers(a, b, c):
    if a <= b:
        if b <= c:
            return a, b, c
        elif a <= c:
            return a, c, b
        else:
            return c, a, b
    else:
        if a <= c:
            return b, a, c
        elif b <= c:
            return b, c, a
        else:
            return c, b, a

if __name__ == '__main__':
    num1 = 34
    num2 = 78
    num3 = 56
    sorted_nums = sort_three_numbers(num1, num2, num3)
    print(sorted_nums)