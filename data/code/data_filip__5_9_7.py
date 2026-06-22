def capitalize_first(s: str) -> str:
    if not s:
        return ""
    return s[0].upper() + s[1:].lower()

if __name__ == "__main__":
    test_cases = [
        "hELLO wORLD",
        "PYTHON",
        "a",
        "AbC",
        "",
        "123abc",
        "ALL LOWER CASE"
    ]
    for case in test_cases:
        result = capitalize_first(case)
        print(f"{repr(case)} -> {repr(result)}")