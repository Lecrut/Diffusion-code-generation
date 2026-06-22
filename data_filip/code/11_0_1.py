from collections import Counter

def find_repeated_characters(text):
    counts = Counter(text)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_string = "programming"
    result = find_repeated_characters(sample_string)
    print(result)