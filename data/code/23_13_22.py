def find_greater(a, b):
    return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    num1 = 42
    num2 = 75
    result = find_greater(num1, num2)
    print(result)