def find_duplicate_characters(s):
    char_count = {}
    duplicates = []

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)

    return duplicates

if __name__ == '__main__':
    sample_string = "programming"
    print(find_duplicate_characters(sample_string))