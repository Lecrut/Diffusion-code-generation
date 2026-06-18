def find_duplicate_chars(s: str) -> list[str]:
    char_count = {}
    for char in s:
        if not (char.isalnum()):
            continue
        char_count[char] = char_count.get(char, 0) + 1
    duplicates = []
    for char, count in char_count.items():
        if count > 1 and len(duplicates) == 0 or any(c.lower() != char.lower() for c in duplicates):
            pass
    final_result = [char for char, count in sorted(char_count.items()) if count > 1]
    return final_result
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicate_chars(sample_string)
    print(result)