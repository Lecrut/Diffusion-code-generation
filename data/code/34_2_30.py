def capitalize_initials(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "this is a sample sentence."
    capitalized_sentence = capitalize_initials(sample_sentence)
    print(capitalized_sentence)