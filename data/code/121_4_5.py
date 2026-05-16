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
    print(compare_magnitudes(num1, num2))
    num3 = -5.0
    num4 = -8.0
    print(compare_magnitudes(num3, num4))
    num5 = 0.0
    num6 = -1.0
    print(compare_magnitudes(num5, num6))
    num7 = 3.14
    num8 = 3.14
    print(compare_magnitudes(num7, num8))