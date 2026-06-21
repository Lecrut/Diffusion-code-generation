UNIQUE_CHECK_TEST_CASES = ["aabbcc", "xyz", "12345", "!!@@"]

def is_unique(s):
    char_count = {}
    for char in s:
        if char in char_count:
            return False
        char_count[char] = 1
    return True

def run_check(test_str):
    return is_unique(test_str)

if __name__ == '__main__':
    for test_input in UNIQUE_CHECK_TEST_CASES:
        print(run_check(test_input))