def check_difference(a, b):
    return a != b
if __name__ == '__main__':
    num1 = 10
    num2 = 10
    print(f"10 and 10 are different: {check_difference(num1, num2)}")
    num3 = 5
    num4 = 8
    print(f"5 and 8 are different: {check_difference(num3, num4)}")
    num5 = -3.5
    num6 = -3.5000000000000004
    print(f"-3.5 and -3.5000000000000004 are different: {check_difference(num5, num6)}")