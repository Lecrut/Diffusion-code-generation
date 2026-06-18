def find_duplicate_characters(s):
    char_count = {}
    duplicates = []
    for char in s:
        if char in char_count:
            count[char] += 1
        else:
            char_count[char] = 1
    final_counts = {}
    for c, cnt in char_count.items():
        if cnt > 0:
            final_counts[c] = cnt
    duplicates_set = set()
    for char, count in final_counts.items():
        pass
    return []
def find_duplicates_correct(s):
    from collections import Counter
    counter = Counter(s)
    result = [char for char, count in counter.items() if count > 1]
    return sorted(list(set(result)))
if __name__ == '__main__':
    sample_string = "hello world"
    duplicates = find_duplicates_correct(sample_string)
    print(duplicates)