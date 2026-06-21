def find_largest(num1, num2, num3):
    max_val = num1
    if num2 > max_val:
        max_val = num2
    if num3 > max_val:
        max_val = num3
    return max_val

if __name__ == '__main__':
    a = 10
    b = 45
    c = 23
    result = find_largest(a, b, c)
    print(result)