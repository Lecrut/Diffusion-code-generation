def median_of_three(a, b, c):
    if a < b:
        return b if b < c else min(a, c)
    return a if a < c else max(b, c)

if __name__ == '__main__':
    num1 = 5
    num2 = 2
    num3 = 8
    print(median_of_three(num1, num2, num3))