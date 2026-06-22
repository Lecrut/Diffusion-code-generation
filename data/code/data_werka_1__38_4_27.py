def find_repeated_letters(sentence):
    letter_count = {}
    repeated_letters = set()
    for char in sentence:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_count:
                letter_count[char_lower] += 1
                if letter_count[char_lower] == 2:
                    repeated_letters.add(char_lower)
            else:
                letter_count[char_lower] = 1
    return repeated_letters

if __name__ == '__main__':
    sample_sentence = "A quick brown fox jumps over the lazy dog."
    result = find_repeated_letters(sample_sentence)
    print(result)