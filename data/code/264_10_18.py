def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        if not isinstance(word, str):
            raise ValueError("Invalid input: All words must be strings.")
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

if __name__ == '__main__':
    sample_text = "hello world hello Python python"
    result = word_frequency(sample_text)
    print(result)