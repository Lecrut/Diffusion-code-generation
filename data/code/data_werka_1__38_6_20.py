def count_letter_frequencies(s):
    frequency = {}
    for char in s:
        if char.isalpha():
            char = char.lower()
            frequency[char] = frequency.get(char, 0) + 1
    return {char: freq for char, freq in frequency.items() if freq > 1}

if __name__ == '__main__':
    sample_string = "Hello World! This is a simple test string."
    result = count_letter_frequencies(sample_string)
    print(result)