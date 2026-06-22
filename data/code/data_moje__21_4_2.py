def get_max(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= c:
        return b
    return c

if __name__ == '__main__':
    print(get_max(10, 5, 20))