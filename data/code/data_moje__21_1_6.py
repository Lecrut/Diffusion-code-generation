def find_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == '__main__':
    x = 10
    y = 25
    z = 15
    result = find_max_of_three(x, y, z)
    print(result)