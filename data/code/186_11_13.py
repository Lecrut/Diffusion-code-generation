def order_words(words):
    return sorted(words, reverse=True)

if __name__ == '__main__':
    sample_words = ["orange", "grape", "watermelon", "apple"]
    sorted_list = order_words(sample_words)
    print(sorted_list)