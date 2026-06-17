def collect_punctuation(text):
    punctuation = []
    for char in text:
        if char in '.,!?;:"\'()[]{}':
            punctuation.append(char)
    return punctuation
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test; how are you? (Case matters.)"
    result = collect_punctuation(sample_string)
    print(result)