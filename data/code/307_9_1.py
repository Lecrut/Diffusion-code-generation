def repeat_sequence(sequence, n):
    result = []
    for _ in range(n):
        result.extend(sequence)
    return result
if __name__ == '__main__':
    sequence_to_repeat = [1, 2, 3]
    repetitions = 4
    final_list = repeat_sequence(sequence_to_repeat, repetitions)
    print(final_list)