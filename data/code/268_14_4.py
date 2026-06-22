def find_first_word(words):
    if not isinstance(words, str) or not words.strip():
        raise ValueError("Input must be a non-empty string")
    return words.split()[0]

if __name__ == '__main__':
    sample_words = "Hello   world from Qwen"
    print(find_first_word(sample_words))