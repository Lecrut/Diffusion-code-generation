def compare_magnitudes(a, b):
    if abs(a) > abs(b):
        return a
    elif abs(b) > abs(a):
        return b
    else:
        return a
if __name__ == '__main__':
    num1 = 10.5
    num2 = -12.3
    print(f"Comparing {num1} and {num2}: {compare_magnitudes(num1, num2)}")
    num3 = -5.0
    num4 = -8.0
    print(f"Comparing {num3} and {num4}: {compare_magnitudes(num3, num4)}")
    num5 = 0.0
    num6 = -1.0
    print(f"Comparing {num5} and {num6}: {compare_magnitudes(num5, num6)}")
    num7 = 3.14
    num8 = 3.14
    print(f"Comparing {num7} and {num8}: {compare_magnitudes(num7, num8)}")
    num9 = -100.0
    num10 = 50.0
    print(f"Comparing {num9} and {num10}: {compare_magnitudes(num9, num10)}")