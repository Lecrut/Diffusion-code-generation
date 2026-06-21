def word_exists(words, target):
    return any(word == target for word in words)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry"]
    target_word = "banana"
    print(word_exists(sample_words, target_word))