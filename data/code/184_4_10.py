def check_word_presence(words, target):
    return any(word == target for word in words)

if __name__ == '__main__':
    sample_tuple = ("apple", "banana", "cherry")
    target_word = "banana"
    print(check_word_presence(sample_tuple, target_word))