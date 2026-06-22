def capitalize_first_letter(word):
    return word[0].upper() + word[1:] if word else ''

def capitalize_words(sentence):
    return ' '.join(capitalize_first_letter(word) for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "this is a Sample Sentence with mixed CASE."
    capitalized_sentence = capitalize_words(sample_sentence)
    print(capitalized_sentence)