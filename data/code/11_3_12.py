def get_repeated_char_frequencies(text):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = {}
    for char, count in counts.items():
        if count > 1:
            result[char] = count
    return result

if __name__ == '__main__':
    sample_string = "programming"
    print(get_repeated_char_frequencies(sample_string))
    sample_string = "aabbccdde"
    print(get_repeated_char_frequencies(sample_string))
    sample_string = "hello"
    print(get_repeated_char_frequencies(sample_string))