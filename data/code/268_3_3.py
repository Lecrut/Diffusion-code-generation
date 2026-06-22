def isolate_first_word(sentence):
    words = sentence.split()
    return words[0] if words else ''

if __name__ == '__main__':
    print(isolate_first_word("Hello world from Python"))