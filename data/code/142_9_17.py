def are_booleans_identical(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    val1 = False
    val2 = True
    print(are_booleans_identical(val1, val2))
    val3 = True
    val4 = True
    print(are_booleans_identical(val3, val4))
    val5 = False
    val6 = False
    print(are_booleans_identical(val5, val6))