def case_converter(s):
    lower = ""
    upper = ""
    title = ""
    
    for char in s:
        if char.islower():
            lower += char
            upper += char.upper()
            title += char.upper() if len(title) == 0 else char.lower()
        elif char.isupper():
            lower += char.lower()
            upper += char
            title += char.lower() if len(title) == 0 else char.lower()
        else:
            lower += char
            upper += char
            title += char
    
    return lower, upper, title

if __name__ == '__main__':
    sample_string = "Hello World"
    lower, upper, title = case_converter(sample_string)
    print(lower)
    print(upper)
    print(title)