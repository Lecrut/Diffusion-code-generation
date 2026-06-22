def calculate_phrase_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    return len(phrase)

if __name__ == '__main__':
    sample_input = "Hello, World!"
    length_of_phrase = calculate_phrase_length(sample_input)
    print(length_of_phrase)