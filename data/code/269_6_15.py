punctuation_marks = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def count_punctuation(text):
    punctuation_counts = {mark: 0 for mark in punctuation_marks}
    for char in text:
        if char in punctuation_counts:
            punctuation_counts[char] += 1
    return punctuation_counts

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? Today is 2023."
    result = count_punctuation(sample_string)
    print(result)