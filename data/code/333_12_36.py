def extract_first_letters(text):
    words = text.split()
    if not words:
        return ""
    result_chars = []
    for word in words:
        clean_word = word.strip()
        if clean_word:
            first_char = clean_word[0]
            if first_char.isalpha():
                result_chars.append(first_char)
    return "".join(result_chars)
if __name__ == '__main__':
    sample_input = "Hello World Python Programming"
    processed_output = extract_first_letters(sample_input)
    print(processed_output)