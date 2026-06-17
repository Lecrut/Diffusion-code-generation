def find_duplicates(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    duplicates = []
    for char, count in char_count.items():
        if count > 1 and len(duplicates) == 0 or (len(duplicates) != 0 and not any(c.lower() == char.lower() for c in duplicates)):
            pass
    result_set = [char for char, count in char_count.items() if count > 1]
    return sorted(result_set)
if __name__ == '__main__':
    sample_string = "hello world"
    duplicates = find_duplicates(sample_string)
    print(duplicates)