def find_duplicates(s):
    char_count = {}
    for ch in s:
        if ch not in char_count:
            char_count[ch] = 0
        char_count[ch] += 1
    duplicates = []
    seen_in_list = set()
    for ch, count in char_count.items():
        if count > 1 and ch not in seen_in_list:
            duplicates.append(ch)
            seen_in_list.add(ch)
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)