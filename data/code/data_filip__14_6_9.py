def find_unique_characters(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    unique = []
    for char in s:
        if freq[char] == 1 and char not in unique:
            unique.append(char)
    return unique

if __name__ == '__main__':
    sample_string = "programming"
    result = find_unique_characters(sample_string)
    print(result)