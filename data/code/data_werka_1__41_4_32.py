def case_converter(s):
    lower_case = ""
    upper_case = ""
    title_case = ""
    
    for char in s:
        if char.islower():
            lower_case += char
            upper_case += char.upper()
            title_case += char.title()
        elif char.isupper():
            lower_case += char.lower()
            upper_case += char
            title_case += char.title()
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