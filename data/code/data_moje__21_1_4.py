def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    a = 10
    b = 25
    c = 15
    result = find_maximum(a, b, c)
    print(result)