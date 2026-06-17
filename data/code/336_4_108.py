def find_duplicates(s):
    char_count = {}
    for char in s:
        if char.isalpha():
            count = char_count.get(char, 0) + 1
            char_count[char] = count
    duplicates = [char for char, count in char_count.items() if count > 1]
    return sorted(duplicates)
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)