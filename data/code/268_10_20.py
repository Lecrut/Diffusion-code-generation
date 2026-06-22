def is_whitespace(char):
    return char == ' '

def find_first_word(s):
    if not s:
        raise ValueError("Input string must not be empty")
    
    index = 0
    while index < len(s) and not is_whitespace(s[index]):
        index += 1
    return s[:index]

if __name__ == '__main__':
    sample_string = "Hello world"
    print(find_first_word(sample_string))