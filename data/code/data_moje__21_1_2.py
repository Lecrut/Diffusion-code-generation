def find_max_of_three(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

if __name__ == '__main__':
    num1 = 15
    num2 = 42
    num3 = 9
    result = find_max_of_three(num1, num2, num3)
    print(result)