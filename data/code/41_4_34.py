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
    lower, upper, title = case_converter(sample_string)
    print("Lowercase:", lower)
    print("Uppercase:", upper)
    print("Title Case:", title)