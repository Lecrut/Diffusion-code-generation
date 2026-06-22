def find_greatest(a, b, c):
    greatest = a
    if b > greatest:
        greatest = b
    if c > greatest:
        greatest = c
    return greatest

if __name__ == '__main__':
    result = find_greatest(3, 7, 2)
    print(result)