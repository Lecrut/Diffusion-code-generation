def has_unique_characters(s: str) -> bool:
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    sample_string_1 = "abcdefg"
    sample_string_2 = "hello"
    result_1 = has_unique_characters(sample_string_1)
    result_2 = has_unique_characters(sample_string_2)
    print(result_1)
    print(result_2)