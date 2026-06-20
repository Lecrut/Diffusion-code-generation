def compare_booleans(x: bool, y: bool) -> bool:
    return x == y

if __name__ == '__main__':
    val1 = True
    val2 = False
    result1 = compare_booleans(val1, val2)
    print(result1)

    val3 = False
    val4 = True
    result2 = compare_booleans(val3, val4)
    print(result2)

    val5 = True
    val6 = True
    result3 = compare_booleans(val5, val6)
    print(result3)