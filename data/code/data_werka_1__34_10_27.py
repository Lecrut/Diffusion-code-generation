def capitalize_first_letter(text):
    return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_text = "this is a sample block of text to be processed."
    result = capitalize_first_letter(sample_text)
    print(result)