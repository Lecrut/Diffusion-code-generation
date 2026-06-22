def find_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    result = find_greatest(10, 42, 5)
    print(result)
    result = find_greatest(100, 50, 100)
    print(result)
    result = find_greatest(-5, -10, -1)
    print(result)