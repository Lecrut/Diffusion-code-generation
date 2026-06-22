from collections import Counter

def repeated_char_freq(text: str) -> dict:
    counts = Counter(text)
    return {char: freq for char, freq in counts.items() if freq > 1}

if __name__ == '__main__':
    sample_text = "programming"
    result = repeated_char_freq(sample_text)
    print(result)