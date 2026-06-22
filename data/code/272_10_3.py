def sort_words(words):
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    sorted_words = sort_words(sample_words)
    for word in sorted_words:
        print(word)