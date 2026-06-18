def find_duplicate_chars(s):
    char_count = {}
    duplicates = []
    for char in s:
        if char in char_count:
            count[char] += 1
        else:
            count[char] = 1
    return [char for char, count_val in sorted(char_count.items()) if count_val > 1 and count_val == len(s)]
def find_duplicate_chars_v2(s):
    from collections import Counter
    counts = Counter(s)
    duplicates = []
    for char, count in counts.most_common():
        if count > 1:
            duplicates.append(char)
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_chars_v2(sample_string)
    print(result)