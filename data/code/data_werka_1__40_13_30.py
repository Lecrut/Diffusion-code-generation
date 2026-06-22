def get_first_alpha_character(s):
    for char in s:
        if char.isalpha():
            return char
    return ""

if __name__ == '__main__':
    test_cases = ["123abc", "456789", "!@#Hello", "NoLeadingNumbers", "", " ", "Python3.8"]
    results = {case: get_first_alpha_character(case) for case in test_cases}
    print(results)