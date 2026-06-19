def analyze_letter_frequency(text):
    frequency = {}
    for char in text:
        if 'a' <= char <= 'z':
            lower_char = char.lower()
            frequency[lower_char] = frequency.get(lower_char, 0) + 1
    
    def filter_frequent_letters(freq_dict):
        return {letter: count for letter, count in freq_dict.items() if count > 1}
    
    frequent_letters = filter_frequent_letters(frequency)
    return frequent_letters

if __name__ == '__main__':
    sample_string = "Alphabet soup is a fun dish."
    result = analyze_letter_frequency(sample_string)
    print(result)