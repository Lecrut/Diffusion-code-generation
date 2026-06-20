def reverse_numbers(a, b):
    while a != 0:
        temp = a
        a = b - (b // a) * a
        b = temp
    return b

if __name__ == '__main__':
    num1 = 34
    num2 = 78
    result = reverse_numbers(num1, num2)
    print(result)