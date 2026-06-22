def find_repeated_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeated = [char for char, count in char_count.items() if count > 1]
    return repeated

if __name__ == '__main__':
    test_string = "programming"
    result = find_repeated_characters(test_string)
    print(result)