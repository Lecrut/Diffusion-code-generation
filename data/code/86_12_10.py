def compare_booleans(a: bool, b: bool) -> str:
    return 'Equal' if a == b else 'Not Equal'

if __name__ == '__main__':
    val1_a = True
    val1_b = False
    result1 = compare_booleans(val1_a, val1_b)
    print(f"Comparing {val1_a} and {val1_b}: {result1}")