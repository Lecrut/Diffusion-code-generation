def count_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return len(text.split())

if __name__ == '__main__':
    sample_text = "This is a sample text for testing purposes. It contains several words."
    try:
        word_count = count_words(sample_text)
        print(word_count)
    except Exception as e:
        print(f"An error occurred: {e}")