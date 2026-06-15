import string
def collect_punctuation(text):
    punctuation_set = set()
    for char in text:
        if char in string.punctuation:
            punctuation_set.add(char)
    return sorted(list(punctuation_set))
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with punctuation."
    result = collect_punctuation(sample_string)
    print(result)