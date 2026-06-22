from collections import Counter

def find_repeated_chars(s: str) -> list[str]:
    counts = Counter(s)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    result = find_repeated_chars("programming")
    print(result)