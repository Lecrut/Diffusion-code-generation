def find_maximum(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

if __name__ == '__main__':
    print(find_maximum(3, 7, 2))
    print(find_maximum(-1, -5, -3))
    print(find_maximum(10, 10, 10))