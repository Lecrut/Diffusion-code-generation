def find_unique_chars(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    unique = [char for char, count in freq.items() if count == 1]
    return unique

if __name__ == '__main__':
    sample_string = "hello world"
    result = find_unique_chars(sample_string)
    print(result)