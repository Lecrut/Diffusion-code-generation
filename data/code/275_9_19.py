def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

if __name__ == '__main__':
    sample_string = "The quick brown fox jumps over the lazy dog"
    result = count_characters(sample_string)
    print(result)