def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def calculate_character_frequencies(text):
    freqs = {}
    for char in text:
        if char != ' ':
            freqs[char] = freqs.get(char, 0) + 1
    return freqs

if __name__ == '__main__':
    sample_text = "Hello world! This is a test."
    validate_input(sample_text)
    frequencies = calculate_character_frequencies(sample_text)
    print(frequencies)