def all_distinct_chars(s):
    char_counts = dict()
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    for count in char_counts.values():
        if count > 1:
            return False
    return True

if __name__ == '__main__':
    test_strings = ["abc", "hello", "1234", "aabb"]
    for t in test_strings:
        print(all_distinct_chars(t))