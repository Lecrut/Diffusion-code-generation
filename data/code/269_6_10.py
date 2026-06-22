PUNCTUATION_MARKS = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def count_punctuation(text):
    punctuation_counts = {p: 0 for p in PUNCTUATION_MARKS}
    for char in text:
        if char in punctuation_counts:
            punctuation_counts[char] += 1
    return punctuation_counts

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? Today is 2023."
    result = count_punctuation(sample_string)
    print(result)