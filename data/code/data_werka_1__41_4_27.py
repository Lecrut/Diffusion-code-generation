CASE_LOWER = 32

def case_converter(s):
    lower_case = ""
    upper_case = ""
    title_case = ""
    
    for char in s:
        if 'a' <= char <= 'z':
            lower_case += char
            upper_case += chr(ord(char) - CASE_LOWER)
            title_case += (chr(ord(char) - CASE_LOWER) if len(title_case) == 0 else char)
        elif 'A' <= char <= 'Z':
            lower_case += chr(ord(char) + CASE_LOWER)
            upper_case += char
            title_case += (char if len(title_case) == 0 else chr(ord(char) + CASE_LOWER))
        else:
            lower_case += char
            upper_case += char
            title_case += char
    
    return lower_case, upper_case, title_case

if __name__ == '__main__':
    sample_string = "this is a sample string for testing"
    lower, upper, title = case_converter(sample_string)
    print(lower)
    print(upper)
    print(title)