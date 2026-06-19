def find_repeated_letters(sentence):
    letter_count = {}
    repeated_letters = set()

    for char in sentence.lower():
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
                if letter_count[char] == 2:
                    repeated_letters.add(char)
            else:
                letter_count[char] = 1

    return repeated_letters

if __name__ == '__main__':
    sample_sentence = "This is a simple test sentence."
    result = find_repeated_letters(sample_sentence)
    print(result)