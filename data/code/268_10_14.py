def find_first_word(s):
    word_start = 0
    while word_start < len(s) and s[word_start].isspace():
        word_start += 1
    if word_start == len(s):
        return ""
    
    word_end = word_start + 1
    while word_end < len(s) and not s[word_end].isspace():
        word_end += 1
    
    return s[word_start:word_end]

if __name__ == '__main__':
    sample_string = "   The quick brown fox jumps over the lazy dog"
    print(find_first_word(sample_string))