def reverse_numbers(a, b):
    if a > b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    num1 = 7
    num2 = -4
    result = reverse_numbers(num1, num2)
    print(result)
    
    num3 = 0
    num4 = 15
    result2 = reverse_numbers(num3, num4)
    print(result2)
    
    num5 = 9
    num6 = 9
    result3 = reverse_numbers(num5, num6)
    print(result3)