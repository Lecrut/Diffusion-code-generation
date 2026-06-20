def process_string(input_string):
    words = input_string.split()
    if len(words) < 2:
        raise ValueError("Input must contain at least two words.")
    return words[0], words[-1]

if __name__ == '__main__':
    sample_input = "The quick brown fox jumps over the lazy dog"
    try:
        first, last = process_string(sample_input)
        print(f"First word is {first}, Last word is {last}")
    except ValueError as e:
        print(e)