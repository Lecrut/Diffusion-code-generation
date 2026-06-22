def is_valid_input(words):
    if not isinstance(words, str) or not words.strip():
        raise ValueError("Input must be a non-empty string")

def find_first_word(words):
    is_valid_input(words)
    return words.split()[0]

if __name__ == '__main__':
    sample_words = "Hello   world from Qwen"
    print(find_first_word(sample_words))