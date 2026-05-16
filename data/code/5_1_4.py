def compare_lengths(a, b):
    if a > b:
        return "greater"
    elif a < b:
        return "less"
    else:
        return "equal"
if __name__ == '__main__':
    num1 = 10.5
    num2 = 15.2
    result1 = compare_lengths(num1, num2)
    print(f"Comparing {num1} and {num2}: {result1}")
    num3 = 7.0
    num4 = 7.0
    result2 = compare_lengths(num3, num4)
    print(f"Comparing {num3} and {num4}: {result2}")
    num5 = 22.8
    num6 = 11.1
    result3 = compare_lengths(num5, num6)
    print(f"Comparing {num5} and {num6}: {result3}")