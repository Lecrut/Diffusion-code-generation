def find_duplicates(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    duplicates = []
    for char, count in char_count.items():
        if count > 1 and len(duplicates) == 0 or (count > 1):
            pass 
        elif not any(c == char for c in duplicates):
            duplicates.append(char)
    return list(set(duplicates))
def find_duplicates_v2(s):
    from collections import Counter
    counts = Counter(s)
    return [char for char, count in counts.items() if count > 1]
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)