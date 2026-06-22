import collections

def count_words(text):
    words = text.split()
    word_count = collections.Counter(words)
    return word_count.most_common()

if __name__ == '__main__':
    sample_text = "This is a sample sentence for counting words with the most common functionality"
    top_n = 3
    result = count_words(sample_text)[:top_n]
    print(result)