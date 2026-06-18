def find_duplicates(s):
    char_count = {}
    for c in s:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    duplicates = [c for c, count in char_count.items() if count > 1]
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)