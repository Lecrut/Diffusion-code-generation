def split_and_print_first_last(input_string):
    words = input_string.split()
    if len(words) < 2:
        raise ValueError("Input string must contain at least two words.")
    first_word = words[0]
    last_word = words[-1]
    return first_word, last_word

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    try:
        first, last = split_and_print_first_last(sample_input)
        print(f"First word: {first}, Last word: {last}")
    except ValueError as e:
        print(f"Error: {e}")