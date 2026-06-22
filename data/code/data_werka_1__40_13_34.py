def is_alphabetic(char):
    return char.isalpha()

def get_first_alpha(s):
    if not s:
        return ""
    
    for char in s:
        if is_alphabetic(char):
            return char
    
    return ""

if __name__ == '__main__':
    sample_strings = ["123abc456", "!@#abc", "no leading numbers", " ", "", "Python"]
    results = [get_first_alpha(s) for s in sample_strings]
    print(results)