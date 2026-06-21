def find_chars_appearing_twice(s):
    if not s:
        return []
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    result = [char for char, freq in count.items() if freq == 2]
    result.sort()
    return result

if __name__ == '__main__':
    sample_input = "aabbccddeeffgg"
    output = find_chars_appearing_twice(sample_input)
    print(output)