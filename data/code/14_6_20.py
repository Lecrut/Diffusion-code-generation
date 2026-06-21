def find_unique_characters(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    unique_chars = []
    for char, count in frequency.items():
        if count == 1:
            unique_chars.append(char)
    return unique_chars

if __name__ == '__main__':
    sample_string = "programming"
    result = find_unique_characters(sample_string)
    print(result)