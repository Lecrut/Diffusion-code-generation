from collections import Counter

def find_duplicate_characters(text):
    char_counts = Counter(text)
    duplicates = [char for char, count in char_counts.items() if count > 1]
    return sorted(duplicates)

if __name__ == '__main__':
    sample_text = "hello world"
    print(find_duplicate_characters(sample_text))