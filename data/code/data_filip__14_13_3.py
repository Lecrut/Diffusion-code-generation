def all_characters_distinct(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            return False
        char_counts[char] = 1
    return True

if __name__ == '__main__':
    print(all_characters_distinct("abcde"))
    print(all_characters_distinct("hello"))
    print(all_characters_distinct("12345"))
    print(all_characters_distinct("11234"))
    print(all_characters_distinct(""))
    print(all_characters_distinct("a"))