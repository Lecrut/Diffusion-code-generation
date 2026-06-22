def count_repeated_chars(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    repeated = {}
    for char, count in freq.items():
        if count > 1:
            repeated[char] = count
    return repeated

if __name__ == '__main__':
    sample_string = "hello world"
    result = count_repeated_chars(sample_string)
    print(result)