def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_text = "this is a sample input"
    capitalized_text = capitalize_words(sample_text)
    print(capitalized_text)