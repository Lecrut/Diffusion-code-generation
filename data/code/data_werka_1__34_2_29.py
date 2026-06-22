def capitalize_initials(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "hello world from alibaba cloud"
    print(capitalize_initials(sample_sentence))