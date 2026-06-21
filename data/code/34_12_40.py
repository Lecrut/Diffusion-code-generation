def capitalize_first_letter(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    
    def capitalize_word(word):
        return word[0].upper() + word[1:] if word else ''
    
    words = sentence.split()
    capitalized_words = [capitalize_word(word) for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_sentence = "hello world, this is an example sentence."
    try:
        capitalized_sentence = capitalize_first_letter(sample_sentence)
        print(capitalized_sentence)
    except ValueError as e:
        print(e)