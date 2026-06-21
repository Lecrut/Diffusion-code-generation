def find_unique_characters(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    unique_chars = [char for char, count in frequency.items() if count == 1]
    return unique_chars

if __name__ == '__main__':
    sample_string = "swiss"
    result = find_unique_characters(sample_string)
    print(result)