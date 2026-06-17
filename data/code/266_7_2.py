import collections
def count_words_optimized(text):
    words = text.split()
    return len(words)
if __name__ == '__main__':
    sample_string = "This is an optimized algorithm for counting words in a string"
    count = count_words_optimized(sample_string)
    print(count)