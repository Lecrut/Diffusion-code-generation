def process_string(text):
    formatter_chars = str.maketrans('', '', '!@#$%^&*()_+-=[]{};:",./<>?')
    clean_text = text.translate(formatter_chars)
    clean_text = clean_text.replace(' ', '')
    if not clean_text:
        return 0
    if clean_text.isdigit() or (clean_text.startswith('-') and clean_text[1:].isdigit()):
        return int(clean_text)
    raise ValueError("String contains non-integer characters after removing formatting.")

if __name__ == '__main__':
    sample = "123-456+789!@#"
    result = process_string(sample)
    print(result)