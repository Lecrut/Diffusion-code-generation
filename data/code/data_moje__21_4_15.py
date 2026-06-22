def find_max(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

if __name__ == '__main__':
    result = find_max(10, 20, 15)
    print(result)