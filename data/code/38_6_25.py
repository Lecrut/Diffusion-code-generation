def count_frequent_letters(text):
    FREQUENCY_THRESHOLD = 1
    frequency = {}
    
    for char in text:
        if 'a' <= char <= 'z':
            lower_char = char.lower()
            frequency[lower_char] = frequency.get(lower_char, 0) + 1
    
    return {letter: count for letter, count in frequency.items() if count > FREQUENCY_THRESHOLD}

if __name__ == '__main__':
    SAMPLE_TEXT = "Hello World! This is a test string with some repeated letters."
    result = count_frequent_letters(SAMPLE_TEXT)
    print(result)