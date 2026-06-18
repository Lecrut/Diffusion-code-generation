def find_duplicates(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    duplicates = [char for char, count in char_count.items() if count > 1]
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)