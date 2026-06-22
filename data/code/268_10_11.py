def find_first_word(s):
    if not isinstance(s, str) or len(s.strip()) == 0:
        raise ValueError("Input must be a non-empty string.")
    
    for i, char in enumerate(s):
        if char == ' ':
            return s[:i]
    return s

if __name__ == '__main__':
    sample_string = "The quick brown fox"
    print(find_first_word(sample_string))