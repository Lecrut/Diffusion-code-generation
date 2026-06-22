def count_punctuation(text):
    punctuation_count = {}
    for char in text:
        if char in '.,!?;:()[]{}':
            if char in punctuation_count:
                punctuation_count[char] += 1
            else:
                punctuation_count[char] = 1
    return punctuation_count

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test."
    result = count_punctuation(sample_text)
    print(result)