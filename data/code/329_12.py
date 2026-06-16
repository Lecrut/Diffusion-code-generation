class StringComparer:
    def check_equality(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError("Input strings cannot be None")
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise TypeError("Inputs must be strings")
        return str1.lower() == str2.lower()
if __name__ == '__main__':
    comparer = StringComparer()
    print(f"Test 1 (Equal): {comparer.check_equality('Hello', 'hello')}")
    print(f"Test 2 (Unequal): {comparer.check_equality('World', 'Python')}")
    print(f"Test 3 (Case Insensitive): {comparer.check_equality('Test', 'test')}")
    try:
        comparer.check_equality("Test", None)
    except TypeError as e:
        print(f"Test 4 (None Input Error): Caught expected error: {e}")
    try:
        comparer.check_equality(123, "test")
    except TypeError as e:
        print(f"Test 5 (Non-string Input Error): Caught expected error: {e}")