import string
def analyze_letter_frequency(text):
    frequency = {}
    for char in text:
        if 'a' <= char <= 'z':
            lower_char = char.lower()
            frequency[lower_char] = frequency.get(lower_char, 0) + 1
    frequent_letters = []
    for letter, count in frequency.items():
        if count > 1:
            frequent_letters.append((letter, count))
    return frequent_letters
if __name__ == '__main__':
    sample_string = "Hello World! This is a test string."
    result = analyze_letter_frequency(sample_string)
    for letter, count in result:
        print(f"{letter}: {count}")