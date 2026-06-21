def find_smallest_string(words):
    return min(words)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry"]
    smallest_word = find_smallest_string(sample_words)
    print(smallest_word)