def find_repeated_characters(s):
    from collections import defaultdict
    char_count = defaultdict(int)
    for char in s:
        char_count[char] += 1
    repeated_chars = sorted([char for char, count in char_count.items() if count > 1])
    return repeated_chars
if __name__ == '__main__':
    sample_string = 'example string with some repeated letters'
    result = find_repeated_characters(sample_string)
    print(result)