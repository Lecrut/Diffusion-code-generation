def find_maximum(a, b, c):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value

if __name__ == '__main__':
    print(find_maximum(15, 27, 9))