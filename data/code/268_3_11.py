def extract_initial_token(sentence):
    tokens = sentence.split()
    return tokens[0] if tokens else ''

if __name__ == '__main__':
    test_sentence = "Good morning, everyone!"
    print(extract_initial_token(test_sentence))