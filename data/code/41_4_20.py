def case_converter(s):
    lower_case = ""
    upper_case = ""
    title_case = ""

    for char in s:
        if 'a' <= char <= 'z':
            lower_case += char
            upper_case += chr(ord(char) - 32)
            title_case += (chr(ord(char) - 32) if len(title_case) == 0 else char)
        elif 'A' <= char <= 'Z':
            lower_case += chr(ord(char) + 32)
            upper_case += char
            title_case += (char if len(title_case) == 0 else chr(ord(char) + 32))
        else:
            lower_case += char
            upper_case += char
            title_case += char

    return lower_case, upper_case, title_case

if __name__ == '__main__':
    sample_string = "Hello World!"
    lower, upper, title = case_converter(sample_string)
    print(lower)
    print(upper)
    print(title)