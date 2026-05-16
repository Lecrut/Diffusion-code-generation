def compare_large_integers(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
if __name__ == '__main__':
    num1 = 1234567890123456789
    num2 = 9876543210987654321
    num3 = 1234567890123456789
    num4 = 1234567890123456789
    print(f"Comparing {num1} and {num2}: {compare_large_integers(num1, num2)}")
    print(f"Comparing {num1} and {num3}: {compare_large_integers(num1, num3)}")
    print(f"Comparing {num2} and {num1}: {compare_large_integers(num2, num1)}")
    print(f"Comparing {num4} and {num4}: {compare_large_integers(num4, num4)}")