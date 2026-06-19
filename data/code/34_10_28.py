def capitalize_first_letter(text):
    return text[0].upper() + text[1:] if text else ''

if __name__ == '__main__':
    sample_text = "this is a sample block of text that needs capitalization."
    capitalized_text = capitalize_first_letter(sample_text)
    print(capitalized_text)