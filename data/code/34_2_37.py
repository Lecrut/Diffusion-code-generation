def capitalize_initials(sentence):
    return ' '.join(word[0].upper() + word[1:] if word else '' for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "this is an example of a different implementation"
    capitalized_sentence = capitalize_initials(sample_sentence)
    print(capitalized_sentence)