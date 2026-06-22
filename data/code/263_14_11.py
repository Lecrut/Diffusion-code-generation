def find_largest(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

if __name__ == '__main__':
    num1 = 3.5
    num2 = 2.8
    num3 = 4.1
    largest_num = find_largest(num1, num2, num3)
    print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_num}")