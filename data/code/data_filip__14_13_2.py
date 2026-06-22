def are_all_characters_distinct(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            return False
        char_counts[char] = 1
    return True

if __name__ == '__main__':
    print(are_all_characters_distinct("abcde"))
    print(are_all_characters_distinct("hello"))
    print(are_all_characters_distinct("world"))
    print(are_all_characters_distinct("programming"))