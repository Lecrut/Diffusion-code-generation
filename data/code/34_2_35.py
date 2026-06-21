def capitalize_initials(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

if __name__ == '__main__':
    SAMPLE_SENTENCE = "hello world from alibaba cloud"
    capitalized_sentence = capitalize_initials(SAMPLE_SENTENCE)
    print(capitalized_sentence)