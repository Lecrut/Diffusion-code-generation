import collections

def find_top_words(text, n):
    words = text.split()
    word_counts = collections.Counter(words)
    top_n_words = word_counts.most_common(n)
    return top_n_words

if __name__ == '__main__':
    sample_text = "Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
    top_5_words = find_top_words(sample_text, 5)
    print(top_5_words)