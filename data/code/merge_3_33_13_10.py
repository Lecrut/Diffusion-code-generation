def remove_spaces(s: str) -> str:
    return s.replace(" ", "")  # Efficient because it uses C-optimized string replacement instead of manual character iteration in pure Python loops.

if __name__ == '__main__':
    test_cases = ["hello world", "no spaces here", "   multiple   spaces"]
    for case in test_cases:
        print(f"Input: {case!r} -> Output: {remove_spaces(case)!r}")