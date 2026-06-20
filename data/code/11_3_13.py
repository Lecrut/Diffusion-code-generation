def count_repeated_chars(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    result = {}
    for char, count in counts.items():
        if count > 1:
            result[char] = count
    return result

if __name__ == '__main__':
    sample_string = "programming"
    repeated_chars = count_repeated_chars(sample_string)
    print(repeated_chars)