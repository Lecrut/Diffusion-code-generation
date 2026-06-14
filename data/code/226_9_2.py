def repeat_sequence(sequence, times):
    result = []
    for _ in range(times):
        result.extend(sequence)
    return result
if __name__ == '__main__':
    sequence_to_repeat = [1, 2, 3]
    number_of_repetitions = 10
    final_result = repeat_sequence(sequence_to_repeat, number_of_repetitions)
    print(final_result)