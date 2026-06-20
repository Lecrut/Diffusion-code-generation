def reverse_numbers(a, b):
    a = a + b
    b = a - 2 * b
    a = a - b
    return a, b

if __name__ == '__main__':
    num1 = 30
    num2 = 45
    result = reverse_numbers(num1, num2)
    print(result)