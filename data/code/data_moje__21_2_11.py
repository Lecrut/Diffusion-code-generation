def find_largest(num1, num2, num3):
    if not all(isinstance(n, (int, float)) for n in (num1, num2, num3)):
        raise TypeError("All arguments must be numeric")
    max_val = num1 if num1 > num2 else num2
    return max_val if max_val > num3 else num3

if __name__ == '__main__':
    result = find_largest(10, 25, 15)
    print(result)
    result = find_largest(3.5, 2.1, 4.8)
    print(result)
    result = find_largest(-5, -2, -10)
    print(result)