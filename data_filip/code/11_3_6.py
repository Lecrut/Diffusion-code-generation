def count_repeated_characters(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    result = {}
    for char, count in frequency.items():
        if count > 1:
            result[char] = count
    return result

if __name__ == '__main__':
    sample_string = "programming"
    output = count_repeated_characters(sample_string)
    print(output)