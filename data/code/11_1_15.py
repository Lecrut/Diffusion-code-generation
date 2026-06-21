from collections import Counter

DUPLICATE_THRESHOLD = 1

def find_duplicate_characters(text: str) -> list:
    counts = Counter(text)
    duplicates = [char for char, count in counts.items() if count > DUPLICATE_THRESHOLD]
    return sorted(duplicates)

if __name__ == '__main__':
    sample_text = "hello world"
    result = find_duplicate_characters(sample_text)
    print(result)