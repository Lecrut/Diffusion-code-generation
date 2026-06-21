def find_unique_characters(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    uniques = []
    for char, count in freq.items():
        if count == 1:
            uniques.append(char)
    return uniques

if __name__ == '__main__':
    sample_string = "programming"
    result = find_unique_characters(sample_string)
    print(result)