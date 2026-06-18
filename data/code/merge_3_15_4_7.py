def compare_strings(str1: str, str2: str) -> bool:
    """Check if two strings are equal ignoring case sensitivity."""
    return str1.lower() == str2.lower()

if __name__ == '__main__':
    # Sample test cases with no user input required
    result1 = compare_strings("Hello", "HELLO")
    result2 = compare_strings("Python 3.9", "python 3.9")
    result3 = compare_strings("Test", "test case")

    print(f"'Hello' vs 'HELLO': {result1}")
    print(f'"Python 3.9" vs "python 3.9": {result2}')
    print(f'"Test" vs "test case": {result3}')