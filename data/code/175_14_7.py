def split_sentence(sentence):
    words = []
    word = ""
    for char in sentence:
        if char == " ":
            if word:
                words.append(word)
                word = ""
        else:
            word += char
    if word:
        words.append(word)
    return words

if __name__ == '__main__':
    sample_sentence = "  Hello   world! This is a test. "
    print(split_sentence(sample_sentence))