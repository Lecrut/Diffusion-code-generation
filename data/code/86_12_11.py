def compare_booleans(a: bool, b: bool) -> str:
    comparison_result = 'Equal' if a == b else 'Not Equal'
    return comparison_result

if __name__ == '__main__':
    val1_a = False
    val1_b = False
    result1 = compare_booleans(val1_a, val1_b)
    print(f"Comparing {val1_a} and {val1_b}: {result1}")
    val2_a = True
    val2_b = False
    result2 = compare_booleans(val2_a, val2_b)
    print(f"Comparing {val2_a} and {val2_b}: {result2}")