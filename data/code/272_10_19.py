def alphabetize(words):
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["grape", "orange", "apple", "banana"]
    sorted_words = alphabetize(sample_words)
    for word in sorted_words:
        print(word)