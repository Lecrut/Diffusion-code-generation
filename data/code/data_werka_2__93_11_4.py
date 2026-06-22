def both_false(a: bool, b: bool) -> bool:
    is_a_false = not a
    is_b_false = not b
    return is_a_false and is_b_false

if __name__ == '__main__':
    val1 = False
    val2 = False
    result = both_false(val1, val2)
    print(result)
    
    val3 = True
    val4 = False
    result2 = both_false(val3, val4)
    print(result2)