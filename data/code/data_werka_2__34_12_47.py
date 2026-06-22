def capitalize_first_letter(sentence):
    def capitalize_word(word):
        return word.capitalize() if word else ''
    
    words = sentence.split()
    capitalized_words = [capitalize_word(word) for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_sentence = "this is a test sentence."
    capitalized_sentence = capitalize_first_letter(sample_sentence)
    print(capitalized_sentence)