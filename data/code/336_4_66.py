def find_duplicates(s):
    char_count = {}
    duplicates = set()
    for char in s:
        if char in char_count:
            char_count[char] += 1
            if char_count[char] == 2:
                duplicates.add(char)
        else:
            char_count[char] = 1
    return list(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)