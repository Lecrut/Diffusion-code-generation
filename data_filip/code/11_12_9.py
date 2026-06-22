from collections import Counter

def filter_duplicates(s):
    counts = Counter(s)
    seen = set()
    result = []
    for char in s:
        if counts[char] > 1 and char not in seen:
            result.append(char)
            seen.add(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "programming"
    output = filter_duplicates(sample_text)
    print(output)