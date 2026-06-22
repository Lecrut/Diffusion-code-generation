def find_first_word(s):
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1
    end = start
    while end < len(s) and s[end] != ' ':
        end += 1
    return s[start:end]

if __name__ == '__main__':
    sample_string = "   The quick brown fox"
    print(find_first_word(sample_string))