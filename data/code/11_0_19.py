from collections import Counter

def find_repeated_chars(s: str) -> set:
    counts = Counter(s)
    return {char for char, count in counts.items() if count > 1}

if __name__ == '__main__':
    sample = "hello world"
    print(find_repeated_chars(sample))