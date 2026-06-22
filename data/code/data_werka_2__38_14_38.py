def find_repeated_characters(s):
    from collections import Counter
    char_count = Counter(s)
    repeated_chars = [char for char, count in char_count.items() if count > 1]
    return sorted(repeated_chars)

if __name__ == '__main__':
    test_string = "hello world"
    result = find_repeated_characters(test_string)
    print(result)