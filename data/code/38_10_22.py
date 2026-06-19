def find_repeated_letters(input_string):
    letter_frequency = {}
    for char in input_string:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_frequency:
                letter_frequency[char_lower] += 1
            else:
                letter_frequency[char_lower] = 1
    
    repeated_letters = {char for char, count in letter_frequency.items() if count > 1}
    return repeated_letters

if __name__ == '__main__':
    sample_string_1 = "abracadabra"
    result_1 = find_repeated_letters(sample_string_1)
    print("Repeated letters in", sample_string_1, ":", result_1)

    sample_string_2 = "mississippi"
    result_2 = find_repeated_letters(sample_string_2)
    print("Repeated letters in", sample_string_2, ":", result_2)