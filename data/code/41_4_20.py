def case_converter(s):
    lower_result = ""
    upper_result = ""
    title_result = ""
    capitalize_next = True
    
    for char in s:
        if 'a' <= char <= 'z':
            lower_result += char
            upper_result += chr(ord(char) - 32)
            if capitalize_next:
                title_result += chr(ord(char) - 32)
                capitalize_next = False
            else:
                title_result += char
        elif 'A' <= char <= 'Z':
            lower_result += chr(ord(char) + 32)
            upper_result += char
            if capitalize_next:
                title_result += char
                capitalize_next = False
            else:
                title_result += chr(ord(char) + 32)
        else:
            lower_result += char
            upper_result += char
            title_result += char
            if char in " \t\n\r":
                capitalize_next = True
            else:
                capitalize_next = False
    
    return lower_result, upper_result, title_result

if __name__ == '__main__':
    sample_string = "Hello World"
    lower_val, upper_val, title_val = case_converter(sample_string)
    print(lower_val)
    print(upper_val)
    print(title_val)