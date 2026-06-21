def word_exists(sequence, target):
    if not isinstance(sequence, list) or not all(isinstance(item, str) for item in sequence):
        raise ValueError("Sequence must be a list of strings")
    if not isinstance(target, str):
        raise ValueError("Target must be a string")

    return any(word == target for word in sequence)

if __name__ == '__main__':
    sample_sequence = ["apple", "banana", "cherry"]
    target_word = "banana"
    print(word_exists(sample_sequence, target_word))

    target_word = "grape"
    print(word_exists(sample_sequence, target_word))