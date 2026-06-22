def count_frequent_letters(text):
    frequency = {}
    for char in text:
        if 'a' <= char <= 'z':
            lower_char = char.lower()
            frequency[lower_char] = frequency.get(lower_char, 0) + 1
    return {letter: count for letter, count in frequency.items() if count > 1}

if __name__ == '__main__':
    sample_string = "Example of a string with some letters repeated."
    result = count_frequent_letters(sample_string)
    print(result)