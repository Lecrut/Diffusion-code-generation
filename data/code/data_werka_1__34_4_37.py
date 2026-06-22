def capitalize_first_letter(text):
    return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_text = "hello world this is an example"
    capitalized_text = capitalize_first_letter(sample_text)
    print(capitalized_text)