def compare_quantities(a, b):
    if a < b:
        return (a, b)
    else:
        return (b, a)
if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result1 = compare_quantities(num1, num2)
    print(f"Comparing {num1} and {num2}: {result1}")
    num3 = -3
    num4 = 7
    result2 = compare_quantities(num3, num4)
    print(f"Comparing {num3} and {num4}: {result2}")
    num5 = 42
    num6 = 42
    result3 = compare_quantities(num5, num6)
    print(f"Comparing {num5} and {num6}: {result3}")