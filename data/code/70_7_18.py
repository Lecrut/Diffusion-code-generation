def process_string(input_string):
    words = input_string.split()
    if words:
        return words[0], words[-1]
    else:
        return None, None

if __name__ == '__main__':
    sample_input = "Hello world this is a test string"
    first_word, last_word = process_string(sample_input)
    print(f"First word: {first_word}, Last word: {last_word}")