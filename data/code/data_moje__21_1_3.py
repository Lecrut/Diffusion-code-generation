def find_max_of_three(a, b, c):
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result

if __name__ == '__main__':
    x = 10
    y = 45
    z = 23
    print(find_max_of_three(x, y, z))