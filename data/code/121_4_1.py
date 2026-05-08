def compare_magnitudes(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a
if __name__ == '__main__':
    num1 = 123.45
    num2 = -67.89
    print(f"Comparing {num1} and {num2}: {compare_magnitudes(num1, num2)}")
    num3 = -10.5
    num4 = -5.2
    print(f"Comparing {num3} and {num4}: {compare_magnitudes(num3, num4)}")
    num5 = 0.0
    num6 = -3.14
    print(f"Comparing {num5} and {num6}: {compare_magnitudes(num5, num6)}")
    num7 = 99.9
    num8 = 100.0
    print(f"Comparing {num7} and {num8}: {compare_magnitudes(num7, num8)}")