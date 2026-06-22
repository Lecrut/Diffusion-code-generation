def has_all_unique_characters(s: str) -> bool:
    seen_chars = set()
    for char in s:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True

if __name__ == '__main__':
    sample_string_1 = "abcdef"
    sample_string_2 = "hello"
    result_1 = has_all_unique_characters(sample_string_1)
    result_2 = has_all_unique_characters(sample_string_2)
    print(result_1)
    print(result_2)