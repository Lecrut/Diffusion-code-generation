def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    num1 = 10
    num2 = 25
    num3 = 15
    result = find_largest(num1, num2, num3)
    print(result)