def count_letter_frequencies(s):
    frequency = {}
    for char in s:
        if char.isalpha():
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return {char: count for char, count in frequency.items() if count > 1}
if __name__ == '__main__':
    sample_string = 'Hello World! This is a simple test string.'
    result = count_letter_frequencies(sample_string)
    print(result)