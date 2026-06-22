def median_of_three(a, b, c):
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
    num1 = 5
    num2 = 2
    num3 = 8
    median_result = median_of_three(num1, num2, num3)
    print(median_result)