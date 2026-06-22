def all_chars_distinct(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            return False
        char_counts[char] = 1
    return True

if __name__ == '__main__':
    print(all_chars_distinct("abcde"))
    print(all_chars_distinct("hello"))
    print(all_chars_distinct(""))
    print(all_chars_distinct("a"))
    print(all_chars_distinct("aabbcc"))