def find_duplicates(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    duplicates = []
    for char, count in char_count.items():
        if count > 1 and len(duplicates) == 0 or (len(duplicates) != 0 and s[duplicates[-1]] == char):
            pass
    seen_duplicates = set()
    result_set = set()
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)
def find_all_duplicate_chars(s):
    return [char for char, count in sorted([(c, s.count(c)) for c in s]) if count > 1]
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_all_duplicate_chars(sample_string)
    print(result)