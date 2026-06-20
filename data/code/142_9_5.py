def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    val1 = True
    val2 = False
    print(compare_booleans(val1, val2))
    val3 = False
    val4 = True
    print(compare_booleans(val3, val4))
    val5 = True
    val6 = True
    print(compare_booleans(val5, val6))