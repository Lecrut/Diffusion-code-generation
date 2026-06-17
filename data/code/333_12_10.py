def extract_first_letters(text: str) -> str:
    words = text.split()
    result_chars = []
    for word in words:
        if not word:                                                     
            continue
        letter = word[0].upper()
        if letter.isalpha():
            result_chars.append(letter)
    return ''.join(result_chars)
if __name__ == '__main__':
    sample_input = "Hello World Python Programming"
    output_result = extract_first_letters(sample_input)
    print(output_result)