def case_converter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    lower_case = []
    upper_case = []
    title_case = []

    for i, char in enumerate(s):
        if 'a' <= char <= 'z':
            lower_case.append(char)
            upper_case.append(chr(ord(char) - 32))
            title_case.append(char.upper() if i == 0 or s[i-1].isspace() else char.lower())
        elif 'A' <= char <= 'Z':
            lower_case.append(chr(ord(char) + 32))
            upper_case.append(char)
            title_case.append(char.lower() if i == 0 or s[i-1].isspace() else char.lower())
        else:
            lower_case.append(char)
            upper_case.append(char)
            title_case.append(char)

    return ''.join(lower_case), ''.join(upper_case), ''.join(title_case)

if __name__ == '__main__':
    sample_string = "this is a Sample String for Testing"
    print(case_converter(sample_string))