def find_repeated_letters(input_string):
    THRESHOLD = 1
    letter_counts = {}
    repeated_letters = []

    for char in input_string:
        if char.isalpha():
            lower_char = char.lower()
            letter_counts[lower_char] = letter_counts.get(lower_char, 0) + 1

    for char, count in letter_counts.items():
        if count > THRESHOLD:
            repeated_letters.append(char)

    return repeated_letters

if __name__ == '__main__':
    sample_input = "Alphabet with repeated letters and some single ones."
    result = find_repeated_letters(sample_input)
    print(result)