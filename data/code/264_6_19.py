def find_words_starting_with(text, letter):
    if not isinstance(text, str) or not isinstance(letter, str):
        raise ValueError("Input must be a string.")
    if len(letter) != 1:
        raise ValueError("Letter must be a single character.")
    
    words = text.split()
    result = [word for word in words if word.lower().startswith(letter.lower())]
    return result

if __name__ == '__main__':
    sample_text = "This is a sample sentence for starting with specific letters. Starting with different letters."
    letter_to_find = 's'
    result = find_words_starting_with(sample_text, letter_to_find)
    print(result)