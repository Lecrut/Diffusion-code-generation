def find_repeated_letters(sentence):
    letter_count = {}
    for char in sentence:
        if char.isalpha():
            char_lower = char.lower()
            letter_count[char_lower] = letter_count.get(char_lower, 0) + 1
    
    repeated_letters = {char for char, count in letter_count.items() if count > 1}
    return repeated_letters

if __name__ == '__main__':
    sample_sentence = "A quick brown fox jumps over the lazy dog."
    result = find_repeated_letters(sample_sentence)
    print(result)