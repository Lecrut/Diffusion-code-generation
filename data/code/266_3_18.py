def find_longest_word(words):
    longest_word = max(words, key=len)
    length = len(longest_word)
    return longest_word, length

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    result = find_longest_word(sample_words)
    print(result)