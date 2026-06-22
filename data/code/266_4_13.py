def count_unique_words(text):
    words = text.split()
    return len(set(words))

if __name__ == '__main__':
    sample_text = "hello world hello Python"
    print(count_unique_words(sample_text))