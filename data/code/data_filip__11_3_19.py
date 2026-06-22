def count_repeated_chars(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    result = {}
    for char, count in freq.items():
        if count > 1:
            result[char] = count
    return result

if __name__ == '__main__':
    sample = "programming"
    print(count_repeated_chars(sample))