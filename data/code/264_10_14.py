def clean_text(text):
    return text.lower()

def split_into_words(text):
    return text.split()

def count_word_frequencies(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def word_frequency(text):
    cleaned_text = clean_text(text)
    words = split_into_words(cleaned_text)
    return count_word_frequencies(words)

if __name__ == '__main__':
    sample_text = "Hello world hello Python python"
    result = word_frequency(sample_text)
    print(result)