import collections

TOP_N = 5

def count_words(text):
    words = text.split()
    word_counts = collections.Counter(words)
    return word_counts.most_common(TOP_N)

if __name__ == '__main__':
    sample_string = "this is a sample sentence for counting the most frequent words in a string"
    result = count_words(sample_string)
    print(result)