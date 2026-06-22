def extract_first_word(sentence):
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            return sentence[:i]
    return sentence

if __name__ == '__main__':
    print(extract_first_word("Hello world"))
    print(extract_first_word("Python programming is fun"))
    print(extract_first_word("SingleWord"))
    print(extract_first_word(" "))
    print(extract_first_word(""))