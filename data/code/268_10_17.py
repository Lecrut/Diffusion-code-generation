FIRST_WORD_DELIMITER = ' '

def find_first_word(s):
    index = 0
    while index < len(s) and s[index] != FIRST_WORD_DELIMITER:
        index += 1
    return s[:index]

if __name__ == '__main__':
    sample_string = "Lorem ipsum dolor sit amet"
    print(find_first_word(sample_string))