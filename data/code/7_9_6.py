import string

def has_special_characters(input_string):
    special_chars = set(string.punctuation + string.whitespace)
    return any(char in special_chars for char in input_string)

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Hello!World",
        "NoSpecialChars",
        "Has @ Symbol",
        ""
    ]
    
    results = [has_special_characters(s) for s in sample_strings]
    print(results)