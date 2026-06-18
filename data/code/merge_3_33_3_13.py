def remove_all_spaces(s: str) -> str:
    return ''.join(ch for ch in s if not ch.isspace())

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "  Leading and Trailing Spaces ",
        "No spaces here",
        "Multiple   spaces   between words"
    ]
    results = []
    for case in test_cases:
        result = remove_all_spaces(case)
        results.append(f'"{case}" -> "{result}"')
    
    print('\n'.join(results))