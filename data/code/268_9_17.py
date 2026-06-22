def extract_first_word(sentence):
    words = sentence.split()
    return words[0] if words else ""

if __name__ == '__main__':
    sample_sentence = "你好，世界！"
    print(extract_first_word(sample_sentence))