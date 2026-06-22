def sort_three_numbers(a, b, c):
    if a < b:
        if a < c:
            if b < c:
                return a, b, c
            else:
                return a, c, b
        else:
            return c, a, b
    else:
        if b < c:
            if a < c:
                return b, a, c
            else:
                return b, c, a
        else:
            return c, b, a

if __name__ == '__main__':
    num1 = 34
    num2 = 7
    num3 = 23
    sorted_nums = sort_three_numbers(num1, num2, num3)
    print(sorted_nums)