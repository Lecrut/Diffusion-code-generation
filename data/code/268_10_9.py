def find_first_word(s):
    if not isinstance(s, str) or len(s.strip()) == 0:
        raise ValueError("Input must be a non-empty string")
    
    index = s.find(' ')
    return s[:index] if index != -1 else s

if __name__ == '__main__':
    sample_string = "The quick brown fox"
    print(find_first_word(sample_string))