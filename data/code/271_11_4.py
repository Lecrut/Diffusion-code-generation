def count_chars(text):
    freqs = {}
    for char in text:
        if char != ' ':
            freqs[char] = freqs.get(char, 0) + 1
    return freqs

if __name__ == '__main__':
    sample_text = "Count me in! This is a test."
    print(count_chars(sample_text))