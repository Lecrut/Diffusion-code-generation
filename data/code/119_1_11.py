def reverse_numbers(a, b):
    if a > b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    num1 = 7
    num2 = 3
    result = reverse_numbers(num1, num2)
    print(result)
    
    num3 = -5
    num4 = -9
    result2 = reverse_numbers(num3, num4)
    print(result2)
    
    num5 = 0
    num6 = 0
    result3 = reverse_numbers(num5, num6)
    print(result3)