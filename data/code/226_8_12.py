def repeat_sequence(sequence, repetition_count):
    repeated_list = []
    for _ in range(repetition_count):
        repeated_list.extend(sequence)
    return repeated_list

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    repetition_count = 3
    repeated_keys = repeat_sequence(sample_dict.keys(), repetition_count)
    print(repeated_keys)