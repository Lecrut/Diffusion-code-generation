def extract_first_alpha(s):
    for char in s:
        if char.isalpha():
            return char
    return ""

if __name__ == '__main__':
    sample_strings = ["!@#abc", "123456", "no leading numbers", " ", ""]
    results = [extract_first_alpha(s) for s in sample_strings]
    print(results)