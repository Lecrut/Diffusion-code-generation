from collections import Counter

def most_frequent_chars(phrase):
    char_counts = Counter(phrase)
    max_count = max(char_counts.values())
    return [char for char, count in char_counts.items() if count == max_count]

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(most_frequent_chars(sample_phrase))