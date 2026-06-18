def extract_first_letters(text):
    import re
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    if not words:
        return ""
    result_chars = [word[0] for word in words]
    return ''.join(result_chars)
if __name__ == '__main__':
    sample_input = "Hello, World! This is a test string."
    processed_output = extract_first_letters(sample_input)
    print(processed_output)