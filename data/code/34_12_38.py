def is_valid_sentence(sentence):
    return isinstance(sentence, str)

def capitalize_first_letter(sentence):
    if not is_valid_sentence(sentence):
        raise ValueError("Input must be a string")
    
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_sentence = "hello world, this is an example sentence."
    try:
        capitalized_sentence = capitalize_first_letter(sample_sentence)
        print(capitalized_sentence)
    except ValueError as e:
        print(e)