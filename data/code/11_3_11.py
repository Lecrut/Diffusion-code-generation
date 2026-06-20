from collections import Counter

def get_repeated_char_frequency(s: str) -> dict:
    counts = Counter(s)
    return {char: count for char, count in counts.items() if count > 1}

if __name__ == '__main__':
    result = get_repeated_char_frequency("aabbccdd")
    print(result)