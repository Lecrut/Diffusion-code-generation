def find_first_word(s):
    for i, char in enumerate(s):
        if char == ' ':
            return s[:i]
    return s

if __name__ == '__main__':
    sample_string = "Jump over the lazy dog"
    print(find_first_word(sample_string))