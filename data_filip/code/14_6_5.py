def find_unique_characters(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    unique_chars = [char for char, count in frequency.items() if count == 1]
    return unique_chars

if __name__ == '__main__':
    sample_string = "programming"
    result = find_unique_characters(sample_string)
    print(result)