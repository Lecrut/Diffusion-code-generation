def has_duplicate_chars(s):
    mask = 0
    for char in s:
        bit_position = ord(char) - ord('a')
        if mask & (1 << bit_position):
            return True
        mask |= (1 << bit_position)
    return False

if __name__ == '__main__':
    sample_string = "hello"
    result = has_duplicate_chars(sample_string)
    print(result)