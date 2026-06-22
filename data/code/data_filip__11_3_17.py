def count_repeated_characters(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    result = {}
    for char, count in frequency.items():
        if count > 1:
            result[char] = count
    return result

if __name__ == '__main__':
    sample_string = "programming"
    repeated_counts = count_repeated_characters(sample_string)
    print(repeated_counts)