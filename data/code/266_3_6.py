def find_longest_word(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a list of strings")
    longest_word = max(words, key=len)
    max_length = len(longest_word)
    return longest_word, max_length

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    result = find_longest_word(sample_words)
    print(f"Longest word: {result[0]}, Length: {result[1]}")