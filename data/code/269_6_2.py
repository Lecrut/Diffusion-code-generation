def count_punctuation(text):
    punctuation_counts = {}
    punctuation_marks = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for p in punctuation_marks:
        punctuation_counts[p] = 0
    for char in text:
        if char in punctuation_counts:
            punctuation_counts[char] += 1
    return punctuation_counts
if __name__ == '__main__':
    sample_string = "Hello, world! How are you? Today is 2023."
    result = count_punctuation(sample_string)
    print(result)