def process_string(text):
    words = text.split()
    if not words:
        return None, None
    return words[0], words[-1]

if __name__ == '__main__':
    sample_text = "This is a sample string with many words to test the performance of the word extraction logic."
    first, last = process_string(sample_text)
    print(first)
    print(last)