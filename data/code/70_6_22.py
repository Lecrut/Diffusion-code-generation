def process_string(text):
    words = text.split()
    if not words:
        return None, None
    first_word = words[0]
    last_word = words[-1]
    return first_word, last_word

if __name__ == '__main__':
    sample_text = "Performance is critical when handling large strings in Python applications"
    first, last = process_string(sample_text)
    print(first)
    print(last)