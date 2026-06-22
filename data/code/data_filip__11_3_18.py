def get_repeated_char_frequencies(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return {char: count for char, count in freq.items() if count > 1}

if __name__ == '__main__':
    sample_string = "swiss"
    result = get_repeated_char_frequencies(sample_string)
    print(result)