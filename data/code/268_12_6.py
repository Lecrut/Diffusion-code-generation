def extract_first_word(text):
    words = text.split()
    return words[0] if words else ''
if __name__ == '__main__':
    sentence1 = '  Leading spaces should be ignored. '
    sentence2 = 'Trailing spaces should also be ignored.   '
    sentence3 = 'No spaces here'
    empty_sentence = ''
    print(extract_first_word(sentence1))
    print(extract_first_word(sentence2))
    print(extract_first_word(sentence3))
    print(extract_first_word(empty_sentence))