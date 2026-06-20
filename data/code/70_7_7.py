def get_first_last_word(sentence):
    words = sentence.split()
    if len(words) < 2:
        raise ValueError("Input string must contain at least two words.")
    return words[0], words[-1]

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    try:
        first, last = get_first_last_word(sample_sentence)
        print(f"First word: {first}, Last word: {last}")
    except ValueError as e:
        print(f"Error: {e}")