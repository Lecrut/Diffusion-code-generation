def count_repeated_letters(s):
    from collections import Counter
    char_count = Counter(s.lower())
    repeated_chars = {char: count for char, count in char_count.items() if count > 1}
    return repeated_chars
if __name__ == '__main__':
    sample_string1 = 'hello world'
    sample_string2 = 'programming'
    sample_string3 = 'abcdefg'
    sample_string4 = 'aabbccddeeff'
    print(count_repeated_letters(sample_string1))
    print(count_repeated_letters(sample_string2))
    print(count_repeated_letters(sample_string3))
    print(count_repeated_letters(sample_string4))