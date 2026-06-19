def is_lowercase(char):
    return 'a' <= char <= 'z'

def is_uppercase(char):
    return 'A' <= char <= 'Z'

def to_lowercase(char):
    if is_uppercase(char):
        return chr(ord(char) + 32)
    return char

def to_uppercase(char):
    if is_lowercase(char):
        return chr(ord(char) - 32)
    return char

def case_converter(s):
    lower_case = ""
    upper_case = ""
    title_case = ""
    
    for i, char in enumerate(s):
        lower_case += to_lowercase(char)
        upper_case += to_uppercase(char)
        
        if i == 0 or not s[i-1].isalpha():
            title_case += to_uppercase(char)
        else:
            title_case += to_lowercase(char)
    
    return lower_case, upper_case, title_case

if __name__ == '__main__':
    sample_string = "this is a sample string for testing"
    lower, upper, title = case_converter(sample_string)
    print(lower)
    print(upper)
    print(title)