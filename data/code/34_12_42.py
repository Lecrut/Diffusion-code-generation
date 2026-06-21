def capitalize_first_letter(sentence):
    if not sentence:
        return ''
    
    def capitalize_word(word):
        if not word:
            return word
        return word[0].upper() + word[1:]
    
    words = sentence.split()
    capitalized_words = [capitalize_word(word) for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    SAMPLE_SENTENCE = "hello world, this is an example sentence."
    capitalized_sentence = capitalize_first_letter(SAMPLE_SENTENCE)
    print(capitalized_sentence)