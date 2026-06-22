def capitalize_first_letter(word):
    return word[0].upper() + word[1:] if word else ''

def capitalize_words(sentence):
    return ' '.join(capitalize_first_letter(word) for word in sentence.split())

if __name__ == '__main__':
    sample_string = "hello world! this is a Test string."
    result = capitalize_words(sample_string)
    print(result)