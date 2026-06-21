MATCH_TRUE = True
MATCH_FALSE = False

def compare_booleans(a: bool, b: bool) -> bool:
    return a == MATCH_TRUE and b == MATCH_TRUE or (a == MATCH_FALSE and b == MATCH_FALSE)
if __name__ == '__main__':
    result1 = compare_booleans(True, True)
    result2 = compare_booleans(False, False)
    result3 = compare_booleans(True, False)
    result4 = compare_booleans(False, True)
    print(result1)
    print(result2)
    print(result3)
    print(result4)