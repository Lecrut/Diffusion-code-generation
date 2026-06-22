def find_median(sequence):
    n = len(sequence)
    if n % 2 == 1:
        return sequence[n // 2]
    else:
        middle_left_index = n // 2 - 1
        middle_right_index = n // 2
        return (sequence[middle_left_index] + sequence[middle_right_index]) / 2

if __name__ == '__main__':
    sample_sequence = [3, 7, 5, 9, 1]
    result = find_median(sample_sequence)
    print(result)