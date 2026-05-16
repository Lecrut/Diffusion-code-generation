import string
def count_letter_frequency(text):
    frequency = {}
    for char in text:
        if 'a' <= char.lower() <= 'z':
            lower_char = char.lower()
            frequency[lower_char] = frequency.get(lower_char, 0) + 1
    return frequency
if __name__ == '__main__':
    sample_string = "Hello World! This is a test string."
    frequencies = count_letter_frequency(sample_string)
    result = []
    for letter, count in frequencies.items():
        if count > 1:
            result.append((letter, count))
    print(result)