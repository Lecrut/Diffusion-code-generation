from collections import Counter

def get_repeated_chars(s):
    counts = Counter(s)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_string = "programming"
    result = get_repeated_chars(sample_string)
    print(result)