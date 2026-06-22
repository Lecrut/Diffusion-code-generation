def find_repeated_letters(sentence):
    letter_count = {}
    for char in sentence:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_count:
                letter_count[char_lower] += 1
                if letter_count[char_lower] == 2:
                    yield char_lower
            else:
                letter_count[char_lower] = 1

if __name__ == '__main__':
    sample_sentence = "This is a simple test sentence."
    repeated_letters = set(find_repeated_letters(sample_sentence))
    print(repeated_letters)