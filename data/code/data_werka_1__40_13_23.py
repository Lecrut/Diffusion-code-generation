def first_alpha_character(s):
    for char in s:
        if char.isalpha():
            return char
    return ""

if __name__ == '__main__':
    test_strings = ["123abc", "456def", "!@#GHI", "789jkl", "mnopqr"]
    results = [first_alpha_character(s) for s in test_strings]
    print(results)