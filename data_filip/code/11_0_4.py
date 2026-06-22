from collections import Counter

def find_repeated_characters(text):
    if not text:
        return []
    frequency = Counter(text)
    repeated = [char for char, count in frequency.items() if count > 1]
    return repeated

if __name__ == '__main__':
    sample_string = "programming"
    result = find_repeated_characters(sample_string)
    print(result)