def reverse_numbers(a, b):
    while a != 0:
        temp = a
        a = b - (b // a) * a
        b = temp
    return b

if __name__ == '__main__':
    num1 = 123456789
    num2 = 987654321
    print(reverse_numbers(num1, num2))