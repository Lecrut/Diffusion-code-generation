def find_first_word(s):
    if not isinstance(s, str) or len(s.strip()) == 0:
        raise ValueError("Input must be a non-empty string")
    
    index = 0
    while index < len(s) and s[index] != ' ':
        index += 1
    return s[:index]

if __name__ == '__main__':
    sample_string = "The quick brown fox"
    print(find_first_word(sample_string))