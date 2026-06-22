def find_repeated_letters(sentence):
    letter_count = {}
    repeated_letters = set()

    for char in sentence:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_count:
                letter_count[char_lower] += 1
            else:
                letter_count[char_lower] = 1

    for char, count in letter_count.items():
        if count > 1:
            repeated_letters.add(char)

    return repeated_letters

if __name__ == '__main__':
    sample_sentence = "This is a simple test sentence."
    result = find_repeated_letters(sample_sentence)
    print(result)