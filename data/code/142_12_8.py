def compare_booleans(a: bool, b: bool) -> bool:
    return not (a ^ b)

if __name__ == '__main__':
    val1 = True
    val2 = True
    print(compare_booleans(val1, val2))
    
    val3 = False
    val4 = True
    print(compare_booleans(val3, val4))