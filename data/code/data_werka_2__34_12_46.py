def capitalize_first_letter(sentence):
    SEPARATOR = ' '
    return SEPARATOR.join(word.capitalize() for word in sentence.split(SEPARATOR))

if __name__ == '__main__':
    SAMPLE_SENTENCE = "hello world, this is an example sentence."
    capitalized_sentence = capitalize_first_letter(SAMPLE_SENTENCE)
    print(capitalized_sentence)