def case_converter(s):
    lower = ""
    upper = ""
    title = ""
    
    for char in s:
        if char.isalpha():
            lower += char.lower()
            upper += char.upper()
            if char.islower():
                title += char.upper()
            else:
                title += char.lower()
        else:
            lower += char
            upper += char
            title += char
    
    return lower, upper, title

if __name__ == '__main__':
    sample_string = "Hello World!"
    lower_case, upper_case, title_case = case_converter(sample_string)
    print(lower_case)
    print(upper_case)
    print(title_case)