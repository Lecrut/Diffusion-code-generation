def compare_numeric_values(a, b):
    return a < b
if __name__ == '__main__':
    val1 = 10
    val2 = 5
    result1 = compare_numeric_values(val1, val2)
    print(f"Comparing {val1} and {val2}: {result1}")
    val3 = 7
    val4 = 7
    result2 = compare_numeric_values(val3, val4)
    print(f"Comparing {val3} and {val4}: {result2}")
    val5 = 15.5
    val6 = 15.500000000000002
    result3 = compare_numeric_values(val5, val6)
    print(f"Comparing {val5} and {val6}: {result3}")
    val7 = -3
    val8 = 0
    result4 = compare_numeric_values(val7, val8)
    print(f"Comparing {val7} and {val8}: {result4}")