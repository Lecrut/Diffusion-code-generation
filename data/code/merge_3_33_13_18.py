def remove_spaces(s: str) -> str:
    return "".join(c for c in s if c != " ")

if __name__ == '__main__':
    test_cases = ["Hello World", "No spaces here", "", "Multiple   spaces"]
    for case in test_cases:
        print(f"Input: {case!r} -> Output: {remove_spaces(case)!r}")