def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = []
    for word in words:
        if word:
            capitalized_word = word[0].upper() + word[1:]
            capitalized_words.append(capitalized_word)
        else:
            capitalized_words.append(word)
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_sentence = "an example of a simple sentence."
    capitalized_sentence = capitalize_first_letter(sample_sentence)
    print(capitalized_sentence)