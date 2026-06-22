def extract_first_word(sentence):
    word = ''
    found_space = False
    for char in sentence:
        if not found_space and char == ' ':
            found_space = True
            continue
        if found_space:
            break
        word += char
    return word

if __name__ == '__main__':
    sample_sentence = "Python is great"
    print(extract_first_word(sample_sentence))