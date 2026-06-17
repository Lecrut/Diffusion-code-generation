class StringComparer:
    def check_equality(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError("Input strings cannot be None")
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise TypeError("Inputs must be strings")
        return str1.lower() == str2.lower()
if __name__ == '__main__':
    comparer = StringComparer()
    print(f"Test 1: 'Hello' and 'hello' -> {comparer.check_equality('Hello', 'hello')}")
    print(f"Test 2: 'World' and 'World' -> {comparer.check_equality('World', 'World')}")
    print(f"Test 3: 'Apple' and 'Banana' -> {comparer.check_equality('Apple', 'Banana')}")
    try:
        comparer.check_equality("Test", None)
    except TypeError as e:
        print(f"Test 4 (None input): Caught expected error: {e}")
    try:
        comparer.check_equality(123, "test")
    except TypeError as e:
        print(f"Test 5 (Non-string input): Caught expected error: {e}")
    try:
        comparer.check_equality(None, "test")
    except TypeError as e:
        print(f"Test 6 (None input): Caught expected error: {e}")