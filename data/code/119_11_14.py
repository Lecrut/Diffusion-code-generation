def reverse_numbers(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

if __name__ == '__main__':
    num1 = 10
    num2 = 25
    result = reverse_numbers(num1, num2)
    print(result)