def find_maximum(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num

if __name__ == '__main__':
    result1 = find_maximum(30, 15, 25)
    print(f"Maximum of (30, 15, 25): {result1}")
    result2 = find_maximum(-20, -10, -5)
    print(f"Maximum of (-20, -10, -5): {result2}")
    result3 = find_maximum(7, 7, 7)
    print(f"Maximum of (7, 7, 7): {result3}")