def vowel_frequency_map(text):
    frequency_map = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    text_lower = text.lower()
    for char in text_lower:
        if char in frequency_map:
            frequency_map[char] += 1
    return frequency_map
if __name__ == '__main__':
    sample_string = "Programming is Awesome"
    result = vowel_frequency_map(sample_string)
    print(result)