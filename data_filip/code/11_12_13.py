from collections import Counter

def filter_unique_chars(s):
    counts = Counter(s)
    return ''.join(c for c in s if counts[c] > 1)

if __name__ == '__main__':
    sample_string = "hello world"
    print(filter_unique_chars(sample_string))