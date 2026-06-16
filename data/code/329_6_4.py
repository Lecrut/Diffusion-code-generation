def test_string_equality(str1, str2):
    return str1 == str2
def run_tests():
    test_cases = [
        ("apple", "apple"),
        ("apple", "Apple"),
        ("apple", "apply"),
        ("hello", "world"),
        ("", ""),
        ("a", "a"),
        ("abc", "abcd"),
        ("test", "testing"),
        ("same", "same"),
        ("different", "different"),
    ]
    all_passed = True
    for str1, str2 in test_cases:
        result = test_string_equality(str1, str2)
        if not result:
            print(f"Test failed for: '{str1}' vs '{str2}'")
            all_passed = False
        else:
            print(f"Test passed for: '{str1}' vs '{str2}'")
    if all_passed:
        print("\nAll tests passed successfully.")
    else:
        print("\nSome tests failed.")
if __name__ == '__main__':
    run_tests()