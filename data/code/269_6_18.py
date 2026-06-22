import string

def punctuation_frequency(paragraph):
    frequency = {char: 0 for char in string.punctuation}
    for char in paragraph:
        if char in frequency:
            frequency[char] += 1
    return frequency

if __name__ == '__main__':
    sample_paragraph = "Hello, world! How are you doing today? I hope everything is going well."
    print(punctuation_frequency(sample_paragraph))