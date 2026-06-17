def get_first_letters(text):
    words = text.split()
    result_chars = []
    for word in words:
        if not word:                                                     
            continue
        first_char = word[0]
        if first_char.isalpha():
            result_chars.append(first_char)
    return ''.join(result_chars)
if __name__ == '__main__':
    user_input = "Hello World, this is a test string."
    processed_output = get_first_letters(user_input)
    print(processed_output)