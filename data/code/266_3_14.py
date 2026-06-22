def find_longest_word(words):
    if not words:
        return "", 0
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    result = find_longest_word(sample_words)
    print(f"Longest word: {result[0]}, Length: {result[1]}")