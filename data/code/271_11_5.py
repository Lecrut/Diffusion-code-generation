def character_frequencies(text):
    freqs = {}
    for char in text:
        if char != ' ':
            freqs[char] = freqs.get(char, 0) + 1
    return freqs

if __name__ == '__main__':
    sample_text = "Hello, World!"
    result = character_frequencies(sample_text)
    print(result)