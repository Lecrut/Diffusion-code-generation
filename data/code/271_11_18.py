def character_frequencies(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    freqs = {}
    for char in text:
        if char != ' ':
            freqs[char] = freqs.get(char, 0) + 1
    return freqs

if __name__ == '__main__':
    sample_text = "Hello, World!"
    print(character_frequencies(sample_text))