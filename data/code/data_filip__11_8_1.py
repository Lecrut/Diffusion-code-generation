def find_chars_appearing_twice(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    result = [char for char, count in char_count.items() if count == 2]
    result.sort()
    return result

if __name__ == '__main__':
    sample_string = "programming"
    print(find_chars_appearing_twice(sample_string))