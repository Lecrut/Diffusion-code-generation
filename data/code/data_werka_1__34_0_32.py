def capitalize_first_letter(text):
    return ' '.join(word[0].upper() + word[1:] if word else '' for word in text.split())

if __name__ == '__main__':
    sample_text = "hello world! this is a TEST string."
    capitalized_text = capitalize_first_letter(sample_text)
    print(capitalized_text)