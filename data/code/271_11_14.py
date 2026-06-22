def count_characters(text):
    counts = {}
    for char in text:
        if char != ' ':
            counts[char] = counts.get(char, 0) + 1
    return counts

if __name__ == '__main__':
    sample_text = "Hello world! This is a test."
    print(count_characters(sample_text))