import collections
def count_words_optimized(text):
    words = text.split()
    return len(words)
if __name__ == '__main__':
    sample_string = "This is an example string for word counting optimization"
    result = count_words_optimized(sample_string)
    print(result)