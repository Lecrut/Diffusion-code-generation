def count_repeated_chars(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    repeated = {char: count for char, count in char_count.items() if count > 1}
    return repeated

if __name__ == '__main__':
    sample_string = "hello world"
    result = count_repeated_chars(sample_string)
    print(result)