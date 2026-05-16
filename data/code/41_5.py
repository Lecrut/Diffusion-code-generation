def case_converter(s):
    lowercase_s = ""
    uppercase_s = ""
    titlecase_s = ""
    for char in s:
        lowercase_s += char.lower()
        uppercase_s += char.upper()
    for i, char in enumerate(s):
        if i == 0:
            titlecase_s += char.upper()
        else:
            titlecase_s += char.lower()
    return lowercase_s, uppercase_s, titlecase_s
if __name__ == '__main__':
    sample_string = "HeLlO WoRlD"
    lower, upper, title = case_converter(sample_string)
    print(f"Original: {sample_string}")
    print(f"Lowercase: {lower}")
    print(f"Uppercase: {upper}")
    print(f"Titlecase: {title}")