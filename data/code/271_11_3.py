def calculate_character_frequencies(text):
    char_freqs = {}
    for character in text:
        if character != ' ':
            if character in char_freqs:
                char_freqs[character] += 1
            else:
                char_freqs[character] = 1
    return char_freqs

if __name__ == '__main__':
    sample_input_text = "This is a test string with some characters."
    frequencies = calculate_character_frequencies(sample_input_text)
    print(frequencies)