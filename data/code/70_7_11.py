def process_string(input_string):
    words = input_string.split()
    if words:
        return words[0], words[-1]
    else:
        return None, None

if __name__ == '__main__':
    sample_string = "This is a sample string for processing"
    first_word, last_word = process_string(sample_string)
    print(f"First word: {first_word}, Last word: {last_word}")