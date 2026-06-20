def process_string(input_string):
    words = input_string.split()
    if len(words) < 2:
        raise ValueError("String must contain at least two words.")
    return words[0], words[-1]

if __name__ == '__main__':
    sample_string = "Hello world this is a test string"
    try:
        first, last = process_string(sample_string)
        print(f"First word: {first}, Last word: {last}")
    except ValueError as e:
        print(f"Error: {e}")