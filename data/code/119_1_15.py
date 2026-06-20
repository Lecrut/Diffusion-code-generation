def reverse_numbers(a, b):
    if a > b:
        return (a, b)
    else:
        return (b, a)
if __name__ == '__main__':
    num1 = 20
    num2 = 7
    result = reverse_numbers(num1, num2)
    print(result)
    num3 = -15
    num4 = -6
    result2 = reverse_numbers(num3, num4)
    print(result2)
    num5 = 30
    num6 = 30
    result3 = reverse_numbers(num5, num6)
    print(result3)