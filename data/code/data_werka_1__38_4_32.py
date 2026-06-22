def find_repeated_letters(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string.")
    
    letter_count = {}
    repeated_letters = set()
    
    for char in sentence:
        if char.isalpha():
            char_lower = char.lower()
            letter_count[char_lower] = letter_count.get(char_lower, 0) + 1
            if letter_count[char_lower] == 2:
                repeated_letters.add(char_lower)
    
    return repeated_letters

if __name__ == '__main__':
    sample_sentence = "This is a simple test sentence with repeated letters."
    try:
        result = find_repeated_letters(sample_sentence)
        print(result)
    except ValueError as e:
        print(e)