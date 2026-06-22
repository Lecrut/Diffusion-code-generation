def split_text_into_words(text):
    words = text.split()
    return words

def count_unique_words(words):
    unique_words = set(words)
    return len(unique_words)

if __name__ == '__main__':
    sample_text = "hello world hello Python"
    words = split_text_into_words(sample_text)
    print(count_unique_words(words))