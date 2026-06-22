def split_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    words = list(text.split())
    if not words:
        raise ValueError("Input string contains no words")
    first_word = words[0]
    last_word = words[-1]
    return first_word, last_word

if __name__ == '__main__':
    sample_data = "Large string processing performance optimization techniques are essential for efficiency"
    start_word, end_word = split_words(sample_data)
    print(start_word)
    print(end_word)