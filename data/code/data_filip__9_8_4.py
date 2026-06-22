def remove_leading_trailing_space(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    test_cases = ["  hello world  ", "\t\n  test  \r\n", "no_spaces", "   "]
    for text in test_cases:
        print(remove_leading_trailing_space(text))