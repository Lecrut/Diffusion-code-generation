def capitalize_first(string):
    if not string:
        return ""
    return string[0].upper() + string[1:].lower()

if __name__ == '__main__':
    test_cases = ["hELLO wORLD", "pyThon", "a", "", "tHiS iS a TeSt"]
    for case in test_cases:
        print(capitalize_first(case))