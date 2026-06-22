def has_distinct_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            return False
        char_count[char] = 1
    return True

if __name__ == '__main__':
    print(has_distinct_characters("abcde"))
    print(has_distinct_characters("hello"))
    print(has_distinct_characters(""))
    print(has_distinct_characters("a"))
    print(has_distinct_characters("aab"))