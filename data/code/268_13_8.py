def extract_first_word(sentence):
    word = ''
    found_space = False
    for char in sentence:
        if char == ' ' and (not found_space):
            found_space = True
            continue
        if found_space:
            break
        word += char
    return word
if __name__ == '__main__':
    sample_sentence = 'Good morning, everyone!'
    first_word = extract_first_word(sample_sentence)
    print(first_word)