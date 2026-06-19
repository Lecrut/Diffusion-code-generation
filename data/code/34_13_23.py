def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "this is a test sentence"
    capitalized_sentence = capitalize_words(sample_sentence)
    print(capitalized_sentence)