def remove_consecutive_spaces(text):
    return ' '.join(text.split())

if __name__ == '__main__':
    sample_text = "This  is   a    test     string."
    cleaned_text = remove_consecutive_spaces(sample_text)
    print(cleaned_text)