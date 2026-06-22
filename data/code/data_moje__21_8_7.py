def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    value1 = 10
    value2 = 25
    value3 = 15
    result = find_largest(value1, value2, value3)
    print(result)