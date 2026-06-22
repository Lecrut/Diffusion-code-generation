def find_first_unique_character(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    for index, char in enumerate(text):
        if frequency[char] == 1:
            return char
    return None

if __name__ == '__main__':
    sample_string = "swiss"
    result = find_first_unique_character(sample_string)
    print(result)