def reverse_numbers(a, b):
    a = a * 2
    b = (a - b) / 2
    a = a - b
    return int(a), int(b)

if __name__ == '__main__':
    num1 = 40
    num2 = 65
    result = reverse_numbers(num1, num2)
    print(result)