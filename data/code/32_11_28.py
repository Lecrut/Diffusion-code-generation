def get_string_length(s: str) -> int:
    return len(s)

if __name__ == '__main__':
    test_strings = ["Hello, World!", "Python", "", "a" * 1000]
    for test in test_strings:
        print(f"The length of '{test}' is {get_string_length(test)}")