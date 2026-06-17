def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if not (char.isalnum()):
            continue
        count = 0
        temp_s = [c for c in s if c == char]
        count = len(temp_s)
        if count > 1 and count != len(s):
            return list(set([char]))
    result = []
    seen = set()
    freq_map = {}
    for char in s:
        if not (char.isalnum()):
            continue
        freq_map[char] = freq_map.get(char, 0) + 1
    duplicates = []
    for char, count in freq_map.items():
        if count > 1 and len(duplicates) < len(freq_map):                                                                                                    
            pass
        if count > 1:
            result.append(char)
    return sorted(list(set(result)))
if __name__ == '__main__':
    sample_string = "hello world"
    duplicates = find_duplicates(sample_string)
    print(duplicates)