def repeat_dictionary_keys(dictionary, repetition_count):
    if not isinstance(dictionary, dict):
        raise ValueError("Input must be a dictionary.")
    if not isinstance(repetition_count, int) or repetition_count < 0:
        raise ValueError("Repetition count must be a non-negative integer.")

    repeated_keys = []
    for _ in range(repetition_count):
        repeated_keys.extend(list(dictionary.keys()))

    return repeated_keys

if __name__ == '__main__':
    sample_dictionary = {'a': 1, 'b': 2, 'c': 3}
    repetition_count = 5
    result = repeat_dictionary_keys(sample_dictionary, repetition_count)
    print(result)