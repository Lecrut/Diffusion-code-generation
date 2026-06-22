def filter_duplicate_chars(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    seen = set()
    for char in s:
        if counts[char] > 1 and char not in seen:
            result.append(char)
            seen.add(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "programming"
    print(filter_duplicate_chars(sample_string))
    sample_string2 = "hello world"
    print(filter_duplicate_chars(sample_string2))
    sample_string3 = "abcdef"
    print(filter_duplicate_chars(sample_string3))