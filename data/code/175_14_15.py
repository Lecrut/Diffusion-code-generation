def split_sentence(sentence):
    words = []
    word = ""
    for char in sentence:
        if char != " ":
            word += char
        elif word:
            words.append(word)
            word = ""
    if word:
        words.append(word)
    return words

if __name__ == '__main__':
    sample_sentence = "  Hello   world! This is a test.  "
    print(split_sentence(sample_sentence))