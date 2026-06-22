def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    result = maximum(10, 20, 15)
    print(result)