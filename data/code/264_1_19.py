import re

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

if __name__ == '__main__':
    sample_text = "Hello world! This is a test string with numbers 123 and symbols @#."
    result = word_frequency(sample_text)
    print(f"Input: '{sample_text}'")
    print(f"Output: {result}")