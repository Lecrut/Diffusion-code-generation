import string

def punctuation_frequency(paragraph):
    freq = {p: 0 for p in string.punctuation}
    for char in paragraph:
        if char in freq:
            freq[char] += 1
    return freq

if __name__ == '__main__':
    sample_paragraph = "Hello, world! How's it going? It's a fine day, isn't it?"
    print(punctuation_frequency(sample_paragraph))