def get_repeated_char_frequencies(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return {char: count for char, count in freq.items() if count > 1}

if __name__ == '__main__':
    sample_text = "hello world"
    result = get_repeated_char_frequencies(sample_text)
    print(result)