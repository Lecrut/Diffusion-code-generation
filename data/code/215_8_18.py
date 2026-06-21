def find_maximum(a, b, c):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value

if __name__ == '__main__':
    result1 = find_maximum(15, 25, 35)
    print(f"Maximum of (15, 25, 35): {result1}")
    result2 = find_maximum(-10, -5, -20)
    print(f"Maximum of (-10, -5, -20): {result2}")
    result3 = find_maximum(7, 7, 7)
    print(f"Maximum of (7, 7, 7): {result3}")