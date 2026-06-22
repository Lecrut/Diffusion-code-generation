from collections import Counter

def get_top_n_words(text, n):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(n)

if __name__ == '__main__':
    sample_string = "This is an example sentence for getting the top N most frequent words"
    top_3_words = get_top_n_words(sample_string, 3)
    print(top_3_words)