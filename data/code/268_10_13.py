def find_first_word(s):
    if not isinstance(s, str) or not s:
        raise ValueError("Input must be a non-empty string")
    
    for i in range(len(s)):
        if s[i] == ' ':
            return s[:i]
    return s

if __name__ == '__main__':
    sample_string = "The quick brown fox"
    print(find_first_word(sample_string))