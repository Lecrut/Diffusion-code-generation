def get_repeated_chars_frequency(s: str) -> dict:
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    result = {}
    for char, count in frequency.items():
        if count > 1:
            result[char] = count
    return result

if __name__ == '__main__':
    sample_string = "programming"
    output = get_repeated_chars_frequency(sample_string)
    print(output)