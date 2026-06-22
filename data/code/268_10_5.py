MAX_WORD_LENGTH = 100

def find_first_word(s):
    for i in range(min(MAX_WORD_LENGTH, len(s))):
        if s[i] == ' ':
            return s[:i]
    return s

if __name__ == '__main__':
    sample_string = "The quick brown fox jumps over the lazy dog"
    print(find_first_word(sample_string))