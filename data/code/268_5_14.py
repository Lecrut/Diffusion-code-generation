def find_first_word(text):
    if not text or text.isspace():
        return ''
    word_start = 0
    for i, char in enumerate(text):
        if char != ' ':
            word_start = i
            break
    for i in range(word_start + 1, len(text)):
        if text[i] == ' ':
            return text[word_start:i]
    return text[word_start:]
if __name__ == '__main__':
    sample_text = 'multiple   spaces here'
    result = find_first_word(sample_text)
    print(result)