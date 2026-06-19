def is_valid_word(word):
    return any(char.isalpha() for char in word)

def extract_first_letter(word):
    return next((char for char in word if char.isalpha()), None)

def get_first_letters(text):
    result = {}
    words = text.split()
    for word in words:
        if is_valid_word(word):
            first_letter = extract_first_letter(word)
            cleaned_word = ''.join(char for char in word if char.isalpha())
            if cleaned_word and first_letter:
                result[cleaned_word] = first_letter
    return result

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with punctuation."
    output_dict = get_first_letters(sample_string)
    print(output_dict)