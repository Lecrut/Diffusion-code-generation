def extract_first_word(s):
    i = 0
    while i < len(s) and s[i] != ' ':
        i += 1
    return s[:i]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print(extract_first_word(sample_string))