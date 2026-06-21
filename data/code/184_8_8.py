def word_exists(sequence, target):
    if not all(isinstance(item, str) for item in sequence):
        raise ValueError("Sequence must contain only strings")
    return any(word == target for word in sequence)

if __name__ == '__main__':
    sample_sequence = ["apple", "banana", "cherry"]
    target_word = "banana"
    print(word_exists(sample_sequence, target_word))

    sample_sequence2 = [1, 2, 3, "banana"]
    try:
        print(word_exists(sample_sequence2, "banana"))
    except ValueError as e:
        print(e)