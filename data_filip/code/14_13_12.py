def all_characters_distinct(s):
    char_count = {}
    for char in s:
        if char in char_count:
            return False
        char_count[char] = 1
    return True

if __name__ == '__main__':
    print(all_characters_distinct("abcde"))
    print(all_characters_distinct("hello"))
    print(all_characters_distinct("Python"))
    print(all_characters_distinct(""))
    print(all_characters_distinct("a"))