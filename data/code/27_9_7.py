def compare_numeric_values(a, b):
    return a < b
if __name__ == '__main__':
    val1 = 10
    val2 = 5
    result1 = compare_numeric_values(val1, val2)
    print(f"Comparing {val1} and {val2}: {result1}")
    val3 = 3.14
    val4 = 3.1400000000000001
    result2 = compare_numeric_values(val3, val4)
    print(f"Comparing {val3} and {val4}: {result2}")
    val5 = -5
    val6 = -10
    result3 = compare_numeric_values(val5, val6)
    print(f"Comparing {val5} and {val6}: {result3}")