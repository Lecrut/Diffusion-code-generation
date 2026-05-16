def reverse_numbers(a, b):
    if a > b:
        return (a, b)
    else:
        return (b, a)
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result = reverse_numbers(num1, num2)
    print(result)
    num3 = -3
    num4 = -7
    result2 = reverse_numbers(num3, num4)
    print(result2)
    num5 = 22
    num6 = 22
    result3 = reverse_numbers(num5, num6)
    print(result3)