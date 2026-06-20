def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    val1 = True
    val2 = False
    result1 = compare_booleans(val1, val2)
    print(f"Comparing {val1} and {val2}: {result1}")
    
    val3 = False
    val4 = False
    result2 = compare_booleans(val3, val4)
    print(f"Comparing {val3} and {val4}: {result2}")
    
    val5 = True
    val6 = True
    result3 = compare_booleans(val5, val6)
    print(f"Comparing {val5} and {val6}: {result3}")