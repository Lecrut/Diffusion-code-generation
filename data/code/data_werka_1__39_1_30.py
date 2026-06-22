import re

def extract_non_overlapping_occurrences(text, pattern):
    return re.findall(pattern, text)

if __name__ == '__main__':
    sample_input = "The quick brown fox jumps over the lazy dog. The fox was very quick."
    patterns = {
        'quick': r'\bquick\b',
        'fox': r'\bfox\b'
    }
    
    for word, pattern in patterns.items():
        result = extract_non_overlapping_occurrences(sample_input, pattern)
        print(f"Occurrences of '{word}': {result}")