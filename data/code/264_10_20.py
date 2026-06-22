def clean_text(text):
    words = text.lower().split()
    return words

def word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

if __name__ == '__main__':
    sample_text = "Hello world hello Python python"
    cleaned_words = clean_text(sample_text)
    result = word_frequency(cleaned_words)
    print(result)