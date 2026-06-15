def order_words(word_list):
    return sorted(word_list)
if __name__ == '__main__':
    sample_words = ["apple", "zebra", "banana", "cat", "dog"]
    sorted_words = order_words(sample_words)
    print(sorted_words)