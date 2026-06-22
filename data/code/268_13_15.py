MAX_LENGTH = 1024

def extract_first_word(sentence):
    word = ''
    for i in range(min(len(sentence), MAX_LENGTH)):
        if sentence[i] == ' ':
            break
        word += sentence[i]
    return word

if __name__ == '__main__':
    sample_sentence = "Hello, world!"
    print(extract_first_word(sample_sentence))