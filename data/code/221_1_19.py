def median_of_three(a, b, c):
    if a < b:
        if b < c:
            return b
        elif a < c:
            return c
        else:
            return a
    else:
        if a < c:
            return a
        elif b < c:
            return c
        else:
            return b

if __name__ == '__main__':
    num1 = 3
    num2 = 7
    num3 = 5
    median_result = median_of_three(num1, num2, num3)
    print(median_result)