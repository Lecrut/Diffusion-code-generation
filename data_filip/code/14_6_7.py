def find_unique_characters(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    unique_chars = [char for char, count in freq.items() if count == 1]
    return unique_chars

if __name__ == '__main__':
    sample_string = "hello world"
    result = find_unique_characters(sample_string)
    print(result)