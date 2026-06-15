def vowel_frequency_map(text):
    frequency = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    text = text.lower()
    for char in text:
        if char in frequency:
            frequency[char] += 1
    return frequency
if __name__ == '__main__':
    sample_string = "Programming is Awesome"
    result = vowel_frequency_map(sample_string)
    print(result)