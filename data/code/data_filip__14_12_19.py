def has_duplicate_chars(s):
    bit_vector = 0
    for char in s:
        bit_index = ord(char) - ord('a')
        if (bit_vector & (1 << bit_index)) > 0:
            return True
        bit_vector |= (1 << bit_index)
    return False

if __name__ == '__main__':
    test_strings = ["abc", "hello", "python", "code"]
    for test in test_strings:
        print(f"{test}: {has_duplicate_chars(test)}")