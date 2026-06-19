def find_repeated_letters(sentence):
    letter_count = {}
    ALPHABETIC_THRESHOLD = 1
    
    for char in sentence:
        if char.isalpha():
            char_lower = char.lower()
            letter_count[char_lower] = letter_count.get(char_lower, 0) + 1

    repeated_letters = {char for char, count in letter_count.items() if count > ALPHABETIC_THRESHOLD}
    return repeated_letters

if __name__ == '__main__':
    sample_sentence = "This is a unique example sentence with several letters."
    result = find_repeated_letters(sample_sentence)
    print(result)