import string

def count_punctuation(text):
    punctuation_counts = {p: 0 for p in string.punctuation}
    for char in text:
        if char in punctuation_counts:
            punctuation_counts[char] += 1
    return {k: v for k, v in punctuation_counts.items() if v > 0}

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? Today is 2023."
    result = count_punctuation(sample_string)
    print(result)