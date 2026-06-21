def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word[0].upper() + word[1:] if word else '' for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_sentence = "hello world, this is an example sentence."
    capitalized_sentence = capitalize_first_letter(sample_sentence)
    print(capitalized_sentence)