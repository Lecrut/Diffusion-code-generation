def compare_lengths(a, b):
    diff = abs(a - b)
    if a > b:
        return (diff, "a is greater")
    elif b > a:
        return (diff, "b is greater")
    else:
        return (diff, "lengths are equal")
if __name__ == '__main__':
    num1 = 10.5
    num2 = 15.2
    result1 = compare_lengths(num1, num2)
    print(f"Comparing {num1} and {num2}: Difference = {result1[0]}, {result1[1]}")
    num3 = 7.0
    num4 = 7.0
    result2 = compare_lengths(num3, num4)
    print(f"Comparing {num3} and {num4}: Difference = {result2[0]}, {result2[1]}")
    num5 = 20.1
    num6 = 19.8
    result3 = compare_lengths(num5, num6)
    print(f"Comparing {num5} and {num6}: Difference = {result3[0]}, {result3[1]}")