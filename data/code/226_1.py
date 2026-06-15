def repeat_sequence(sequence, count):
    result = []
    for _ in range(count):
        result.extend(sequence)
    return result
if __name__ == '__main__':
    start_seq = [1, 2]
    repetition_count = 3
    output = repeat_sequence(start_seq, repetition_count)
    print(output)