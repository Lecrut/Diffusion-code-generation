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
    num4 = -1.0
    print(compare_magnitudes(num3, num4))
    num5 = 0.0
    num6 = -0.001
    print(compare_magnitudes(num5, num6))
    num7 = 99.9
    num8 = 100.0
    print(compare_magnitudes(num7, num8))