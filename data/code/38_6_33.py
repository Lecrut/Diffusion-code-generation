def count_letter_frequencies(s):
    frequency = {}
    for char in s:
        if char.isalpha():
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return {char: freq for char, freq in frequency.items() if freq > 1}

if __name__ == '__main__':
    sample_string = "Hello World! This is a test string with some letters repeated."
    result = count_letter_frequencies(sample_string)
    print(result)