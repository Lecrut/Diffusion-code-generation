def char_frequency(text):
    freq = {}
    for char in text:
        if char != ' ':
            freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == '__main__':
    sample_text = "Hello world! This is a test."
    print(char_frequency(sample_text))