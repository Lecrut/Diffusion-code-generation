def capitalize_sentence(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "hello world, this is an example sentence."
    capitalized_sentence = capitalize_sentence(sample_sentence)
    print(capitalized_sentence)