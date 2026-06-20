from collections import Counter

def get_repeated_characters(s):
    counts = Counter(s)
    return sorted([char for char, count in counts.items() if count > 1])

if __name__ == '__main__':
    sample_string = "programming"
    result = get_repeated_characters(sample_string)
    print(result)