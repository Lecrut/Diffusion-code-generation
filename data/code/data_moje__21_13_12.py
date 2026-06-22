def find_maximum(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

if __name__ == '__main__':
    result = find_maximum(3.14, 2.71, 3.15)
    print(result)