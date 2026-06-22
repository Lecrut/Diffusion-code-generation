def capitalize_first_letter(sentence):
    if not sentence:
        return ''
    
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_sentence = "hello world, this is an example sentence."
    capitalized_sentence = capitalize_first_letter(sample_sentence)
    print(capitalized_sentence)