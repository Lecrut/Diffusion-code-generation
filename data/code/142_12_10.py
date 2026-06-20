XOR_TRUE_FALSE = 1

def compare_booleans(a: bool, b: bool) -> bool:
    return (a ^ b) == XOR_TRUE_FALSE

if __name__ == '__main__':
    val1 = True
    val2 = True
    result1 = compare_booleans(val1, val2)
    print(f"Comparing {val1} and {val2}: Result={result1}")

    val3 = False
    val4 = True
    result2 = compare_booleans(val3, val4)
    print(f"Comparing {val3} and {val4}: Result={result2}")