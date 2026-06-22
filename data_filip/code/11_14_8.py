import collections
import string

def find_character_frequency_duplicates(text: str) -> dict:
    if not text:
        return {}
    
    char_counts = collections.Counter(text)
    
    duplicates = {char: count for char, count in char_counts.items() if count > 1}
    
    sorted_duplicates = dict(sorted(duplicates.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_duplicates

if __name__ == '__main__':
    sample_text = "Hello, World! This is a sample text with repeated characters like l and o."
    result = find_character_frequency_duplicates(sample_text)
    print(result)