def find_first_word(s):
    for i in range(len(s)):
        if s[i] == ' ':
            return s[:i]
    return s

if __name__ == '__main__':
    sample_string = "Hello world from Qwen"
    print(find_first_word(sample_string))