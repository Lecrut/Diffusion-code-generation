import math
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
    print(f"Comparing {val1} and {val2}: {result1}")
    val3 = 7.0
    val4 = 7.0
    result2 = compare_lengths(val3, val4)
    print(f"Comparing {val3} and {val4}: {result2}")
    val5 = 20.1
    val6 = 19.8
    result3 = compare_lengths(val5, val6)
    print(f"Comparing {val5} and {val6}: {result3}")