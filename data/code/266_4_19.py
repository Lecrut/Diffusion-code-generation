def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)
if __name__ == '__main__':
    sample_text = 'hello world hello Python'
    result = count_unique_words(sample_text)
    print(result)