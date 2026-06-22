def extract_repeated_chars(s):
    char_counts = {}
    for c in s:
        char_counts[c] = char_counts.get(c, 0) + 1
    unique_chars = set(s)
    repeated = unique_chars.intersection(set(c for c in char_counts if char_counts[c] > 1))
    return sorted(repeated)

if __name__ == '__main__':
    print(extract_repeated_chars("programming"))
    print(extract_repeated_chars("hello"))
    print(extract_repeated_chars("abcdef"))
    print(extract_repeated_chars("aabbccdd"))
    print(extract_repeated_chars("mississippi"))