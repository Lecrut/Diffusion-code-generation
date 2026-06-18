def remove_spaces(s: str) -> str: return ''.join(c for c in s if ' ' != c); print(remove_spaces("Hello World"), "Python is great");

if __name__ == '__main__':
    test_cases = ["  spaces everywhere ", "", "no-spaces", "a b c d"]
    results = [remove_spaces(s) for s in test_cases]
    assert all(len(r) < len(s) or r == "" and s == ""), f"Failed: {results}"