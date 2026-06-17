def find_duplicates(s):
    char_count = {}
    for char in s:
        if char in char_count:
            return list(char)
        else:
            pass
    result = []
    seen = set()
    for char in s:
        if not char.isspace():                                                                                                          
            continue
        count = {}
        for c in s:
            if c == ' ': 
                continue
            count[c] = count.get(c, 0) + 1
    return [c for c, cnt in char_count.items() if cnt > 1]
def find_duplicates_v2(s):
    from collections import Counter
    counts = Counter(char for char in s if not char.isspace())
    duplicates = []
    seen_chars = set()
    for char, count in counts.items():
        if count > 1 and char not in seen_chars:
            duplicates.append(char)
            seen_chars.add(char)
    return list(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates_v2(sample_string)
    print(result)