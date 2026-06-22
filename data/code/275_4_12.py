def are_all_unique(chars):
    char_set = set()
    for char in chars:
        if char in char_set:
            return False
        char_set.add(char)
    return True

if __name__ == '__main__':
    sample_chars1 = "abcdefg"
    print("All unique (sample_chars1):", are_all_unique(sample_chars1))
    sample_chars2 = "hello world"
    print("All unique (sample_chars2):", are_all_unique(sample_chars2))