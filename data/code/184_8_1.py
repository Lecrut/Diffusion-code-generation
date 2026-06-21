def word_exists(sequence, target):
    return any(word == target for word in sequence)

if __name__ == '__main__':
    sample_sequence = ["apple", "banana", "cherry"]
    target_word = "banana"
    print(word_exists(sample_sequence, target_word))