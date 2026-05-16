def compare_numeric_values(a, b):
    return a > b
if __name__ == '__main__':
    val1 = 10
    val2 = 5
    result = compare_numeric_values(val1, val2)
    print(result)
    val3 = 3.14
    val4 = 3.14
    result2 = compare_numeric_values(val3, val4)
    print(result2)
    val5 = -5
    val6 = -10
    result3 = compare_numeric_values(val5, val6)
    print(result3)