def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    result = find_largest(10, 45, 23)
    print(result)