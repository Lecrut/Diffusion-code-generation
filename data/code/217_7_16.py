def compare_numbers(a, b):
    diff = a - b
    sign = (diff >> 63) & 1
    return {'larger': a, 'smaller': b, 'equal': sign == 0}

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result1 = compare_numbers(num1, num2)
    print(f"Comparing {num1} and {num2}: {result1}")
    
    num3 = 7
    num4 = 7
    result2 = compare_numbers(num3, num4)
    print(f"Comparing {num3} and {num4}: {result2}")
    
    num5 = 20
    num6 = 15
    result3 = compare_numbers(num5, num6)
    print(f"Comparing {num5} and {num6}: {result3}")