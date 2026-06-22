def get_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    result = get_largest(3.5, 7.2, 4.9)
    print(result)