MAX_SEARCH_LENGTH = 256

def extract_first_word(sentence):
    word = ''
    index = 0
    while index < len(sentence) and sentence[index] != ' ':
        if index >= MAX_SEARCH_LENGTH:
            break
        word += sentence[index]
        index += 1
    return word

if __name__ == '__main__':
    sample_sentence = "Hello, world!"
    print(extract_first_word(sample_sentence))