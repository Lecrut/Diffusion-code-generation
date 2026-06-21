def find_maximum(a, b, c):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value

if __name__ == '__main__':
    sample1 = find_maximum(15, 25, 35)
    print(f"Maximum of (15, 25, 35): {sample1}")
    
    sample2 = find_maximum(-10, -5, -20)
    print(f"Maximum of (-10, -5, -20): {sample2}")
    
    sample3 = find_maximum(100, 50, 75)
    print(f"Maximum of (100, 50, 75): {sample3}")