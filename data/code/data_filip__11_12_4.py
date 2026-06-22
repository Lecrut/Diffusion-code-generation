from collections import Counter

def filter_unique_characters(s: str) -> str:
    counts = Counter(s)
    result = []
    for char in s:
        if counts[char] > 1:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "programming"
    result = filter_unique_characters(sample_string)
    print(result)