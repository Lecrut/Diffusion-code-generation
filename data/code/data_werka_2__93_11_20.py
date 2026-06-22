from typing import Tuple

def both_false(a: bool, b: bool) -> bool:
    lookup = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False,
    }
    return lookup[(a, b)]

if __name__ == '__main__':
    val1 = False
    val2 = False
    result = both_false(val1, val2)
    print(result)
    val3 = True
    val4 = False
    result2 = both_false(val3, val4)
    print(result2)
    val5 = False
    val6 = True
    result3 = both_false(val5, val6)
    print(result3)
    val7 = True
    val8 = True
    result4 = both_false(val7, val8)
    print(result4)