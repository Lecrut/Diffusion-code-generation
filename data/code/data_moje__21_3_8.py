def find_max(a, b, c):
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result

if __name__ == '__main__':
    print(find_max(3.14, 2.71, 9.81))