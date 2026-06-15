import collections
text = "this is a sample sentence for word counting"
words = text.lower().split()
word_counts = collections.Counter(words)
if __name__ == '__main__':
    print(word_counts)