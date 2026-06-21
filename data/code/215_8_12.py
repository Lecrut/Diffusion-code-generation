def find_maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

if __name__ == '__main__':
    result1 = find_maximum(10, 20, 30)
    print(f"Maximum of (10, 20, 30): {result1}")
    result2 = find_maximum(40, 5, 15)
    print(f"Maximum of (40, 5, 15): {result2}")
    result3 = find_maximum(-10, -20, -5)
    print(f"Maximum of (-10, -20, -5): {result3}")