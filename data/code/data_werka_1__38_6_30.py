def is_valid_letter(char):
    return 'a' <= char <= 'z'

def count_frequencies(text):
    frequency = {}
    for char in text:
        if is_valid_letter(char):
            lower_char = char.lower()
            frequency[lower_char] = frequency.get(lower_char, 0) + 1
    return frequency

def filter_frequent_letters(frequency):
    frequent_letters = [(letter, count) for letter, count in frequency.items() if count > 1]
    return frequent_letters

if __name__ == '__main__':
    sample_string = "Hello World! This is a test string."
    frequencies = count_frequencies(sample_string)
    result = filter_frequent_letters(frequencies)
    for letter, count in result:
        print(f"{letter}: {count}")