def extract_first_word(s):
    for i in range(len(s)):
        if s[i] == ' ':
            return s[:i]
    return s

if __name__ == '__main__':
    print(extract_first_word("Hello world"))
    print(extract_first_word("Python programming is fun"))
    print(extract_first_word("SingleWord"))
    print(extract_first_word(" "))
    print(extract_first_word(""))