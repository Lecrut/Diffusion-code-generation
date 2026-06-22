def find_chars_appearing_twice(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    result = [char for char, count in char_count.items() if count == 2]
    result.sort()
    return result

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "aabbccdd",
        "abcabcabc",
        "pythonprogramming",
        "charactercounting",
        "no_duplicates_here"
    ]
    for test_str in sample_strings:
        print(find_chars_appearing_twice(test_str))