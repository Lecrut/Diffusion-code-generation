def has_unique_chars(s: str) -> bool:
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if checker & (1 << val):
            return False
        checker |= 1 << val
    return True

if __name__ == '__main__':
    sample_1 = "abcdefg"
    sample_2 = "hello"
    result_1 = has_unique_chars(sample_1)
    result_2 = has_unique_chars(sample_2)
    print(result_1)
    print(result_2)