def check_strict_inequality(a, b):
    result = a > b
    print(result)
    return result
if __name__ == '__main__':
    val1 = True
    val2 = False
    check_strict_inequality(val1, val2)
    val3 = False
    val4 = True
    check_strict_inequality(val3, val4)
    val5 = True
    val6 = True
    check_strict_inequality(val5, val6)