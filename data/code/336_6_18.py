import sys
def is_unique(s: str) -> bool:
    return len(set(s)) == len(s)
if __name__ == '__main__':
    sample = "abcdef" if not hasattr(sys.stdin.read, 'read') else None                                                               
    test_cases = [
        ("abc", True),
        ("aabb", False),
        ("1234567890", True),
        ("hello", False)
    ]
    all_passed = True
    for s, expected in test_cases:
        result = is_unique(s)
        if result != expected:
            print(f"FAIL: '{s}' -> {result}, expected {expected}")
            sys.exit(1)
    final_check = is_unique("unique")
    print(f"Final Check 'unique': {final_check}")