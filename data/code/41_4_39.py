def case_converter(s):
    LOWERCASE_START = ord('a')
    UPPERCASE_START = ord('A')
    CASE_DIFFERENCE = 32
    lower_case = []
    upper_case = []
    title_case = []
    capitalize_next = True
    for char in s:
        if LOWERCASE_START <= ord(char) <= LOWERCASE_START + 25:
            lower_case.append(char)
            upper_case.append(chr(ord(char) - CASE_DIFFERENCE))
            if capitalize_next:
                title_case.append(chr(ord(char) - CASE_DIFFERENCE))
                capitalize_next = False
            else:
                title_case.append(char)
        elif UPPERCASE_START <= ord(char) <= UPPERCASE_START + 25:
            lower_case.append(chr(ord(char) + CASE_DIFFERENCE))
            upper_case.append(char)
            if capitalize_next:
                title_case.append(char)
                capitalize_next = False
            else:
                title_case.append(chr(ord(char) + CASE_DIFFERENCE))
        else:
            lower_case.append(char)
            upper_case.append(char)
            title_case.append(char)
    return (''.join(lower_case), ''.join(upper_case), ''.join(title_case))
if __name__ == '__main__':
    sample_string = 'Hello, World!'
    lower, upper, title = case_converter(sample_string)
    print(lower)
    print(upper)
    print(title)