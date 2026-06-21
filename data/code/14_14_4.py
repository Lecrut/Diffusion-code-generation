def has_unique_chars_sorting(s: str) -> bool:
    if not s:
        return True
    sorted_chars = sorted(s)
    for i in range(len(sorted_chars) - 1):
        if sorted_chars[i] == sorted_chars[i + 1]:
            return False
    return True

if __name__ == '__main__':
    print(has_unique_chars_sorting('abcdefg'))
    print(has_unique_chars_sorting('hello'))
    print(has_unique_chars_sorting(''))
    print(has_unique_chars_sorting('a'))
    print(has_unique_chars_sorting('aabbc'))