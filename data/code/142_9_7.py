def are_booleans_identical(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    val1 = True
    val2 = False
    print(are_booleans_identical(val1, val2))
    val3 = False
    val4 = True
    print(are_booleans_identical(val3, val4))
    val5 = True
    val6 = True
    print(are_booleans_identical(val5, val6))