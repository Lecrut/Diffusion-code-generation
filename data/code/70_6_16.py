def process_string(text):
    words = text.split()
    if not words:
        return None, None
    return words[0], words[-1]

if __name__ == '__main__':
    sample_text = "This is a sample string with several words for testing purposes"
    first, last = process_string(sample_text)
    print(first)
    print(last)