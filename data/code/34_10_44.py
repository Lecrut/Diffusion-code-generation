def capitalize_first_letter(s):
    return s[0].upper() + s[1:] if s else ''

def capitalize_sentence(sentence):
    words = sentence.split()
    capitalized_words = [capitalize_first_letter(word) for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_string = "embracing new challenges in ai development"
    result = capitalize_sentence(sample_string)
    print(result)