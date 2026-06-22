def title_case_string(s):
    if not s:
        return s
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    sample1 = "hELLO wORLD"
    sample2 = "pyThOn"
    sample3 = ""
    sample4 = "a"
    print(title_case_string(sample1))
    print(title_case_string(sample2))
    print(title_case_string(sample3))
    print(title_case_string(sample4))