def extract_boundary_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    word_list = text.split()
    if not word_list:
        return None, None
    first_word = word_list[0]
    last_word = word_list[-1]
    return first_word, last_word

if __name__ == '__main__':
    sample_data = "Performance optimization is critical for large inputs and efficient memory usage"
    start, end = extract_boundary_words(sample_data)
    print(start)
    print(end)