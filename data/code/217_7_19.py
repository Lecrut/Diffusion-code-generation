def is_greater(a, b):
    return (a - b) >> 31 & 1

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result1 = "greater" if is_greater(num1, num2) else "not greater"
    print(f"Comparing {num1} and {num2}: {result1}")
    num3 = 7
    num4 = 7
    result2 = "greater" if is_greater(num3, num4) else "not greater"
    print(f"Comparing {num3} and {num4}: {result2}")
    num5 = 20
    num6 = 15
    result3 = "greater" if is_greater(num5, num6) else "not greater"
    print(f"Comparing {num5} and {num6}: {result3}")