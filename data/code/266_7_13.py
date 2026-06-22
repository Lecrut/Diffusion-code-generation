import collections

def most_frequent_words(text, n=10):
    words = text.split()
    word_counts = collections.Counter(words)
    return word_counts.most_common(n)

if __name__ == '__main__':
    sample_text = "this is an example sentence for the most frequent word counting"
    top_n_words = most_frequent_words(sample_text, n=3)
    print(top_n_words)