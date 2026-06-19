def analyze_letter_frequency(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    frequency = {}
    for char in text:
        if 'a' <= char <= 'z':
            lower_char = char.lower()
            frequency[lower_char] = frequency.get(lower_char, 0) + 1
    
    frequent_letters = [(letter, count) for letter, count in frequency.items() if count > 1]
    return frequent_letters

if __name__ == '__main__':
    sample_string = "Hello World! This is a test string."
    try:
        result = analyze_letter_frequency(sample_string)
        for letter, count in result:
            print(f"{letter}: {count}")
    except ValueError as e:
        print(e)