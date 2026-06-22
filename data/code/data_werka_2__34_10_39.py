def capitalize_each_word(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

if __name__ == '__main__':
    sample_text = "innovating with artificial intelligence"
    capitalized_text = capitalize_each_word(sample_text)
    print(capitalized_text)