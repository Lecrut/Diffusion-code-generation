def compare_numeric_values(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
if __name__ == '__main__':
    val1 = 10
    val2 = 5
    result1 = compare_numeric_values(val1, val2)
    print(f"Comparing {val1} and {val2}: {result1}")
    val3 = 7
    val4 = 7
    result2 = compare_numeric_values(val3, val4)
    print(f"Comparing {val3} and {val4}: {result2}")
    val5 = 20
    val6 = 30
    result3 = compare_numeric_values(val5, val6)
    print(f"Comparing {val5} and {val6}: {result3}")