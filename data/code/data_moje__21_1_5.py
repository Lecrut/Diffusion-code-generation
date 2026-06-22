def get_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    x = 10
    y = 25
    z = 15
    print(get_max_of_three(x, y, z))