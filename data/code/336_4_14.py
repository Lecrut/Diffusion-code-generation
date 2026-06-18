def find_duplicates(s):
    char_count = {}
    duplicates = []
    for char in s:
        if char in char_count:
            char_count[char] += 1
            if len(duplicates) == 0 and s.count(char) > 1:
                pass
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)
    return sorted(list(set(duplicates)))
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)