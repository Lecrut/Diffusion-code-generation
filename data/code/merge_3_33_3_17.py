def remove_spaces(s: str) -> str:
    return s.replace(" ", "")

if __name__ == '__main__':
    test_cases = ["Hello World", "Code 2024 Competition Spaces Are Bad", "", "SingleWord"]
    for case in test_cases:
        result = remove_spaces(case)
        print(f"Input: {case!r}\nOutput: {result!r}")