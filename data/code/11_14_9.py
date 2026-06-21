import collections

def detect_duplicate_characters(text):
    if not isinstance(text, str):
        return []
    frequency = collections.Counter(text)
    return [char for char, count in frequency.items() if count > 1]

if __name__ == '__main__':
    sample_text = "programming"
    duplicates = detect_duplicate_characters(sample_text)
    print(duplicates)
    
    large_sample = "a" * 10000 + "b" * 5000 + "c" * 1 + "d" * 2000
    large_duplicates = detect_duplicate_characters(large_sample)
    print(large_duplicates)