def find_duplicates(s):
    char_count = {}
    for ch in s:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    return [ch for ch, count in char_count.items() if count > 1]
if __name__ == '__main__':
    sample_string = "hello world"
    result = find_duplicates(sample_string)
    print(result)