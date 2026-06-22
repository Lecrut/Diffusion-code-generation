def count_words(s):
    words = s.lower().split()
    return len(words)

if __name__ == '__main__':
    sample_text = "This is a Sample text with Mixed Case letters and punctuation."
    word_count = count_words(sample_text)
    print(word_count)