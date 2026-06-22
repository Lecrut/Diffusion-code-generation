def capitalize_first_letter(text):
    return ' '.join(word[0].upper() + word[1:] for word in text.split())

if __name__ == '__main__':
    sample_text = "hello world! this is a TEST."
    result = capitalize_first_letter(sample_text)
    print(result)