def reverse_numbers(a, b):
    a = a - b
    b = a + 2 * b
    a = b - a
    return a, b

if __name__ == '__main__':
    num1 = 7
    num2 = 3
    result = reverse_numbers(num1, num2)
    print(result)