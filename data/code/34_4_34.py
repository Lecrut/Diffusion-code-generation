def capitalize_first_letter(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_text = "hello world from alibaba cloud"
    result = capitalize_first_letter(sample_text)
    print(result)