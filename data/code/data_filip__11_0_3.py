from collections import Counter

def find_repeated_characters(s: str) -> list:
    char_counts = Counter(s)
    repeated = [char for char, count in char_counts.items() if count > 1]
    repeated.sort(key=lambda char: s.index(char))
    return repeated

if __name__ == '__main__':
    sample_string = "programming"
    result = find_repeated_characters(sample_string)
    print(result)