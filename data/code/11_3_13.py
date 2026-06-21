from collections import Counter

def repeated_char_frequencies(s: str) -> dict:
    counts = Counter(s)
    return {char: count for char, count in counts.items() if count > 1}

if __name__ == '__main__':
    test_string = "programming"
    result = repeated_char_frequencies(test_string)
    print(result)