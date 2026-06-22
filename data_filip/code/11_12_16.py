def filter_duplicate_characters(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    result = [char for char, count in char_count.items() if count > 1]
    return result

if __name__ == '__main__':
    sample_string = "hello world"
    duplicates = filter_duplicate_characters(sample_string)
    print(duplicates)