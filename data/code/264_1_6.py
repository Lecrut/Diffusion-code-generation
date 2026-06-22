def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

if __name__ == '__main__':
    sample_string = "Hello world! This is a test string with numbers 123 and symbols @#$."
    result = word_frequency(sample_string)
    print(result)