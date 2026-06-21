def has_all_unique_characters(s):
    seen_characters = set()
    for char in s:
        if char in seen_characters:
            return False
        seen_characters.add(char)
    return True

if __name__ == '__main__':
    sample_string_1 = "abcdef"
    sample_string_2 = "hello"
    result_1 = has_all_unique_characters(sample_string_1)
    result_2 = has_all_unique_characters(sample_string_2)
    print(result_1)
    print(result_2)