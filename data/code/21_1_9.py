def find_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    num1 = 10
    num2 = 25
    num3 = 15
    result = find_max_of_three(num1, num2, num3)
    print(result)