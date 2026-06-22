def find_longest_word(words):
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    longest_word, length = find_longest_word(sample_words)
    print(f"Longest word: {longest_word}, Length: {length}")