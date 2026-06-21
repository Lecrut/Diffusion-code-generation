def capitalize_initial_letters(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

if __name__ == '__main__':
    SAMPLE_SENTENCE = "hello world from alibaba cloud"
    capitalized_sentence = capitalize_initial_letters(SAMPLE_SENTENCE)
    print(capitalized_sentence)