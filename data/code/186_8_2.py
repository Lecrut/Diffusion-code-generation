def sort_by_length(words):
    return sorted(words, key=len)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    print(sort_by_length(sample_words))