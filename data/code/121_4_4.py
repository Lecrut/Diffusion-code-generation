def compare_magnitudes(a, b):
    if abs(a) > abs(b):
        return a
    elif abs(b) > abs(a):
        return b
    else:
        return a
if __name__ == '__main__':
    num1 = 10.5
    num2 = -15.2
    print(f"Comparing {num1} and {num2}: {compare_magnitudes(num1, num2)}")
    num3 = -5.0
    num4 = -2.5
    print(f"Comparing {num3} and {num4}: {compare_magnitudes(num3, num4)}")
    num5 = 0.0
    num6 = -3.14
    print(f"Comparing {num5} and {num6}: {compare_magnitudes(num5, num6)}")
    num7 = 100.0
    num8 = 99.99999999999999
    print(f"Comparing {num7} and {num8}: {compare_magnitudes(num7, num8)}")