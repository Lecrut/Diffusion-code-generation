def get_highest_value(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    result = get_highest_value(10.5, 20.3, 15.1)
    print(result)