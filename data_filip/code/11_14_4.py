import collections

def find_duplicate_char_frequencies(text):
    if not text:
        return {}
    char_counts = collections.Counter(text)
    freq_map = collections.defaultdict(list)
    for char, count in char_counts.items():
        freq_map[count].append(char)
    duplicates = {}
    for freq, chars in freq_map.items():
        if len(chars) > 1:
            duplicates[freq] = sorted(chars)
    return duplicates

if __name__ == '__main__':
    sample_text = "aabbccddeeffgggghhhhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyz"
    result = find_duplicate_char_frequencies(sample_text)
    print(result)