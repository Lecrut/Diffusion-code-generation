def get_string_length(s: str) -> int:
    return len(s)

if __name__ == '__main__':
    test_cases = ["", "hello world", "Python\nProgramming", "\t"]
    for case in test_cases:
        print(f"Length of '{case}': {get_string_length(case)}")