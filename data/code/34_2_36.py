def capitalize_initials(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_sentence = "welcome to the world of programming"
    result = capitalize_initials(sample_sentence)
    print(result)