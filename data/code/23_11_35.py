def greater_of_two(a, b):
    return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    num1 = 42
    num2 = 27
    result = greater_of_two(num1, num2)
    print(result)