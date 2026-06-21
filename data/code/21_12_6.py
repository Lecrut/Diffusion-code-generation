def get_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    result = get_greatest(10, 25, 3)
    print(result)