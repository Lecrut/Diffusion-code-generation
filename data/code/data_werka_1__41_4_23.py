def case_converter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    lower_case = ""
    upper_case = ""
    title_case = ""
    capitalize_next = True

    for char in s:
        if 'a' <= char <= 'z':
            lower_case += char
            upper_case += chr(ord(char) - 32)
            if capitalize_next:
                title_case += chr(ord(char) - 32)
                capitalize_next = False
            else:
                title_case += char
        elif 'A' <= char <= 'Z':
            lower_case += chr(ord(char) + 32)
            upper_case += char
            if capitalize_next:
                title_case += char
                capitalize_next = False
            else:
                title_case += chr(ord(char) + 32)
        else:
            lower_case += char
            upper_case += char
            title_case += char
            if char.isspace():
                capitalize_next = True

    return lower_case, upper_case, title_case

if __name__ == '__main__':
    sample_string = "this is a Sample STRING for Testing"
    lower, upper, title = case_converter(sample_string)
    print(lower)
    print(upper)
    print(title)