def capitalize_first_letter(text):
    words = text.split()
    capitalized_words = [word[0].upper() + word[1:] if word else '' for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_text = "this is a block of text that needs capitalization"
    result = capitalize_first_letter(sample_text)
    print(result)