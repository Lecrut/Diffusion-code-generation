def capitalize_first_letter(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

if __name__ == '__main__':
    sample_string = "this is an example string"
    capitalized_string = capitalize_first_letter(sample_string)
    print(capitalized_string)