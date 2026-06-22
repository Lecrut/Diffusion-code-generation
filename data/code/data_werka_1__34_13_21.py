def capitalize_first_letter(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "hello world this is a test"
    capitalized_sentence = capitalize_first_letter(sample_sentence)
    print(capitalized_sentence)