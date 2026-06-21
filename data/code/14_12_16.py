def has_duplicate_chars(s: str) -> bool:
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if checker & 1 << val:
            return True
        checker |= 1 << val
    return False
if __name__ == '__main__':
    samples = ['abcdef', 'hello', 'programming', 'abcdefg', 'aabbcc', 'python', 'duplicate', '']
    for sample in samples:
        result = has_duplicate_chars(sample)
        print(f"String '{sample}': {result}")