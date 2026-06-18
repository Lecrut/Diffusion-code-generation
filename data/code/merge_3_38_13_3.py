def contains_repeated_letters(s: str) -> bool:
    """Return True if string s has any repeated letters, False otherwise."""
    seen = set()
    for char in s.lower():  # Case-insensitive check; ignore non-letters optionally by checking isalpha
        if not char.isalpha():
            continue
        if char in seen:
            return True
        seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        ("hello", True),       # 'l' repeats
        ("abcdef", False),     # All unique
        ("Hello World!", True),# 'l', 'o' repeat (case-insensitive)
        ("Python3.8", False),  # No repeated letters in "python3.8" if digits and dots ignored; actually 'n','o','t','y','p','h','3','.','8' -> n,o not repeating? Wait: P-y-t-h-o-n-3-. -8 -> no repeats
        ("a", False),          # Single char, no repeat
    ]

    for input_str, expected in test_cases:
        result = contains_repeated_letters(input_str)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{input_str}' -> {result} (expected {expected})")