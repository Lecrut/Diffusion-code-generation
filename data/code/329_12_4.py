class StringComparer:
    def check_equality(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise TypeError("Both inputs must be strings.")
        return str1.lower() == str2.lower()
if __name__ == '__main__':
    comparer = StringComparer()
    print(f"Test 1: 'Hello' and 'hello' -> {comparer.check_equality('Hello', 'hello')}")
    print(f"Test 2: 'World' and 'Other' -> {comparer.check_equality('World', 'Other')}")
    print(f"Test 3: 'a' and 'A' -> {comparer.check_equality('a', 'A')}")
    try:
        comparer.check_equality("test", None)
    except TypeError as e:
        print(f"Test 4 (Error Handling): Caught expected error: {e}")
    try:
        comparer.check_equality(123, "test")
    except TypeError as e:
        print(f"Test 5 (Error Handling): Caught expected error: {e}")