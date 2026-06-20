TRUE = True
FALSE = False

def compare_booleans(flag1: bool, flag2: bool) -> bool:
    return flag1 == flag2

if __name__ == '__main__':
    result1 = compare_booleans(TRUE, TRUE)
    result2 = compare_booleans(FALSE, FALSE)
    result3 = compare_booleans(TRUE, FALSE)
    print(result1)
    print(result2)
    print(result3)