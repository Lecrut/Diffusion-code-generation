def find_unique_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

if __name__ == '__main__':
    sample_string = "swiss"
    result = find_unique_char(sample_string)
    print(result)