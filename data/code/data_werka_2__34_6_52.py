def capitalize_first_letter(text):
    return text.title()

if __name__ == '__main__':
    sample_text = "hello world this is a test"
    capitalized_text = capitalize_first_letter(sample_text)
    print(capitalized_text)