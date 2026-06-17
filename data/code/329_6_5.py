def test_string_equality(str1, str2):
    return str1 == str2
def run_tests():
    test_cases = [
        ("hello", "hello"),
        ("hello", "world"),
        ("abc", "abc"),
        ("abc", "abd"),
        ("apple", "apply"),
        ("Apple", "apple"),
        ("test", "test "),
        ("", ""),
        ("a", "b"),
        ("longerstring", "short"),
        ("same", "same"),
        ("123", "123"),
        ("a", "A"),
    ]
    all_passed = True
    for str1, str2 in test_cases:
        result = test_string_equality(str1, str2)
        expected = str1 == str2
        if result != expected:
            print(f"Test failed for: '{str1}' vs '{str2}'. Expected: {expected}, Got: {result}")
            all_passed = False
        else:
            print(f"Test passed for: '{str1}' vs '{str2}'")
    if all_passed:
        print("\nAll tests passed successfully.")
    else:
        print("\nSome tests failed.")
if __name__ == '__main__':
    run_tests()