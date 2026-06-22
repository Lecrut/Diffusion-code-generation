def extract_first_word(sentence):
    word = ''
    for char in sentence:
        if char == ' ':
            break
        word += char
    return word

if __name__ == '__main__':
    print(extract_first_word('Hello, world!'))