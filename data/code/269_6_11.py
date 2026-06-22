import string

def punctuation_frequency(paragraph):
    freq = {punct: 0 for punct in string.punctuation}
    for char in paragraph:
        if char in freq:
            freq[char] += 1
    return freq

if __name__ == '__main__':
    sample_paragraph = "Hello, world! How are you? I'm fine. Thanks!"
    print(punctuation_frequency(sample_paragraph))