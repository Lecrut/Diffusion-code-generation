def capitalize_first_char(s: str) -> str:
    if not s:
        return ""
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    test_cases = ["hELLO wORLD", "python", "a", "", "ALLCAPS", "MiXeD CaSe"]
    for case in test_cases:
        result = capitalize_first_char(case)
        print(result)