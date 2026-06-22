def find_repeated_characters(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    result = [char for char, cnt in count.items() if cnt > 1]
    return result

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcabc",
        "abcdef",
        "aabbcc",
        "programming",
        ""
    ]
    for test_string in sample_strings:
        print(find_repeated_characters(test_string))