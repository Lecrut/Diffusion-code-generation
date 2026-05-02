def compare_lengths(a: float, b: float) -> tuple[float, str]:
    diff = abs(a - b)
    if a > b:
        return (diff, "a is greater")
    elif b > a:
        return (diff, "b is greater")
    else:
        return (diff, "lengths are equal")
if __name__ == '__main__':
    val1 = 10.5
    val2 = 15.2
    result1 = compare_lengths(val1, val2)
    print(f"Comparing {val1} and {val2}: Difference = {result1[0]}, Result = {result1[1]}")
    val3 = 3.14159
    val4 = 3.14158
    result2 = compare_lengths(val3, val4)
    print(f"Comparing {val3} and {val4}: Difference = {result2[0]}, Result = {result2[1]}")
    val5 = 7.0
    val6 = 7.0
    result3 = compare_lengths(val5, val6)
    print(f"Comparing {val5} and {val6}: Difference = {result3[0]}, Result = {result3[1]}")