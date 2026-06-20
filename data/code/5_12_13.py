def capitalize_first_letter(s):
    if not s:
        return ""
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    test_cases = ["hELLO wORLD", "tHIS is a tEst", "pYTHON", "a", "", "ALLUPPER", "alllower"]
    for case in test_cases:
        result = capitalize_first_letter(case)
        print(result)