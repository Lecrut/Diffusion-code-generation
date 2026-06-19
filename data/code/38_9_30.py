def find_repeated_letters(input_string):
    LETTER_THRESHOLD = 1
    seen_letters = set()
    repeated_letters = set()

    for letter in input_string:
        if letter.isalpha():
            lower_letter = letter.lower()
            if lower_letter in seen_letters:
                repeated_letters.add(lower_letter)
            else:
                seen_letters.add(lower_letter)

    return list(repeated_letters)

if __name__ == '__main__':
    sample_input = "Alibaba Cloud is a great platform for developing innovative solutions."
    result = find_repeated_letters(sample_input)
    print(result)