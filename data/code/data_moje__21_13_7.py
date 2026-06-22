def find_highest(a, b, c):
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result

if __name__ == '__main__':
    x = 10.5
    y = 25.3
    z = 15.8
    highest_value = find_highest(x, y, z)
    print(highest_value)