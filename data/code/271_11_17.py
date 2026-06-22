CHAR_FREQ_MAP = {}

def populate_char_freq_map():
    for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
        CHAR_FREQ_MAP[char] = 0

def calculate_character_frequencies(text):
    freqs = {}
    for char in text:
        if char != ' ' and char in CHAR_FREQ_MAP:
            freqs[char] = freqs.get(char, 0) + 1
    return freqs

if __name__ == '__main__':
    populate_char_freq_map()
    sample_text = "Hello, World! This is a test."
    frequencies = calculate_character_frequencies(sample_text)
    print(frequencies)