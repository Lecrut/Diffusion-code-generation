def process_string(input_string):
    words = input_string.split()
    if len(words) < 2:
        raise ValueError("Input string must contain at least two words.")
    return words[0], words[-1]

if __name__ == '__main__':
    sample_input = "This is a sample sentence for processing."
    try:
        first_word, last_word = process_string(sample_input)
        print(f"First word: {first_word}, Last word: {last_word}")
    except ValueError as e:
        print(f"Error: {e}")