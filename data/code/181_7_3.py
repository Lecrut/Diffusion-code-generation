def count_vowel_frequency(text):
    frequency = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    text_lower = text.lower()
    for char in text_lower:
        if char in frequency:
            frequency[char] += 1
    return frequency
if __name__ == '__main__':
    sample_string = "Programming is Awesome"
    result = count_vowel_frequency(sample_string)
    print(result)