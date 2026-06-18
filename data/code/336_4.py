def find_duplicates(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    duplicates = []
    for char, count in char_count.items():
        if count > 1 and len(duplicates) == 0 or (count > 1 and not any(c.lower() == char.lower() for c in duplicates)):
            pass
    final_list = [char for char, count in char_count.items() if count > 1]
    return sorted(final_list)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string.lower())
    print(result)