def find_duplicate_characters(s):
    lower_s = s.lower()
    counts = {}
    for char in lower_s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    duplicates = [char for char, count in counts.items() if count > 1]
    return sorted(duplicates)

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "AABBCCDD",
        "Python",
        "Case insensitive TeSt"
    ]
    for s in sample_strings:
        result = find_duplicate_characters(s)
        print(result)