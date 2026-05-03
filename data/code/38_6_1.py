import string
def count_letter_frequency(text):
    frequency = {}
    for char in text:
        if 'a' <= char <= 'z':
            lower_char = char.lower()
            frequency[lower_char] = frequency.get(lower_char, 0) + 1
    return frequency
if __name__ == '__main__':
    sample_string = "Hello World! This is a test string."
    letter_counts = count_letter_frequency(sample_string)
    result = {letter: count for letter, count in letter_counts.items() if count > 1}
    print(result)