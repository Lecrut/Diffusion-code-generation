def repeat_sequence(sequence, times):
    result = []
    for _ in range(times):
        result.extend(sequence)
    return result
if __name__ == '__main__':
    sequence_to_repeat = [1, 2, 3]
    repetition_count = 10
    final_result = repeat_sequence(sequence_to_repeat, repetition_count)
    print(final_result)