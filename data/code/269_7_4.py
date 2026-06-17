import string
def collect_punctuation(text):
    punctuation_set = set()
    for char in text:
        if char in string.punctuation:
            punctuation_set.add(char)
    return sorted(list(punctuation_set))
if __name__ == '__main__':
    sample_string1 = "Hello, world! This is a test."
    sample_string2 = "No punctuation here."
    sample_string3 = "What's up? (Is this a question?)"
    result1 = collect_punctuation(sample_string1)
    result2 = collect_punctuation(sample_string2)
    result3 = collect_punctuation(sample_string3)
    print("Sample 1:", result1)
    print("Sample 2:", result2)
    print("Sample 3:", result3)